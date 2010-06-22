"""Setup the drsin application"""
import logging

from drsin.config.environment import load_environment
import drsin.model as model
import sqlite3
from datetime import datetime
log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
	"""Place any commands to setup drsin here"""
	load_environment(conf.global_conf, conf.local_conf)
	# Drop/Create the tables if they don't already exist
	model.metadata.drop_all()
	model.metadata.create_all()
	
	print conf['oldblog.database']
	oldconn = sqlite3.connect(conf['oldblog.database'])
	def dict_factory(cursor, row):
		d = {}
		for idx, col in enumerate(cursor.description):
			d[col[0]] = row[idx]
		return d
	oldconn.row_factory = dict_factory
	oldconn.text_factory = lambda x: unicode(x, "latin1")
	
	log.info("Adding old comments...")
	c = oldconn.cursor()
	c.execute("SELECT * FROM wp_comments")
	commentsMap = {}
	for row in c:
		d = None
		try:
			d = datetime.strptime(str(row['comment_date']), "%Y-%m-%d %H:%M:%S")
		except Exception, e: pass
		spam = 1.0
		ham = 0.1
		if row['comment_approved'] == "1":
			spam = 0.1
			ham = 1.0
		comment = model.Comment(
			author = row['comment_author'],
			email = row['comment_author_email'],
			url = row['comment_author_url'],
			date = d,
			spam=spam,
			ham=ham,
			content =  row['comment_content']
		)
		if row['comment_post_ID'] not in commentsMap:
			commentsMap[row['comment_post_ID']] = []
		commentsMap[row['comment_post_ID']].append(comment)
	
	
	log.info("Adding old categories and keywords...")
	c = oldconn.cursor()
	c.execute("SELECT * FROM wp_terms as t LEFT JOIN wp_term_taxonomy as tt on t.term_id == tt.term_id")
	keywordMap = {}
	categoryMap = {}
	for row in c:
		if row['taxonomy'] == "category":
			categoryMap[row['name']] = model.Category(
				category=row['name']
			)
		else:
			keywordMap[row['name']] = model.Keyword(
				keyword=row['name']
			)
	model.Category(category=u"Default")
	model.session.commit()
	c = oldconn.cursor()
	log.info("Adding old blog posts...")
	c.execute("SELECT * FROM wp_posts")
	for row in c:
		if(row['post_type'] == 'revision'): continue
		# '2003-05-07 12:00:00'
		d = None
		try:
			d = datetime.strptime(str(row['post_date']), "%Y-%m-%d %H:%M:%S")
		except Exception, e: pass
		# Keywords and Categories Query
		q = "select t.name as tn,tt.taxonomy as ttt from wp_posts p  left join wp_term_relationships as tr on tr.object_id = p.id left join wp_term_taxonomy as tt on tt.term_taxonomy_id = tr.term_taxonomy_id left join wp_terms as t on t.term_id = tt.term_id where p.id = " + str(row['ID'])
		qc = oldconn.cursor()
		qc.execute(q)
		keywords = []
		category = None
		for qrow in qc:
			if(qrow['tn'] == None):
				continue
			if(qrow['ttt'] == "category"):
				category = categoryMap[qrow['tn']]
			else:
				keywords.append(keywordMap[qrow['tn']]) 
		
		comments = commentsMap.get(row['ID'],[])
		p = model.Post(
			id=row['ID'],
			content=row['post_content'],
			date=d,
			title=row['post_title'],
			category=category,
			keywords=keywords,
			comments=comments
		)
	log.info("Adding roles and users...")
	sina = model.User()
	sina.username = u"sinjax"
	sina.password = u"thecool2"
	
	model.session.commit()
	
	
