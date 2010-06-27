% if not c.post_list:
<div class="post post_solo" id="post_${c.post.id}">
%else:
<div class="post" id="post_${c.post.id}">
%endif
	<h2 class="post_title">
		<a href="${h.url_for(controller='post',action='show',id=c.post.id)}">${c.post.title}</a>
		<a href="${h.url_for(controller='post',action='show',id=c.post.id)}" title="permalink" alt="permalink"><img src="/graphics/link.png"/></a>
		<a href="" onclick="return false;" title="location" alt="location"><img src="/graphics/globe.png"/></a>
	</h2>
	
	% if "user" in session and session["user"]:
	<script type="text/javascript" charset="utf-8">
		$(document).ready(function  (argument) {
			post = $("#post_${c.post.id}")
			$("#post_${c.post.id} .editlink").click(function (argument) {
				$.get("${h.url_for(controller='post',action='update',id=c.post.id)}",function (data) {
					$("#post_${c.post.id}").html(data)
					return false;
				})
				return false;
			})
		})
	</script>
	<!-- ${session["user"].username} Logged In! -->
	<a class="editlink" href="${h.url_for(controller='post',action='update',id=c.post.id)}"><img src="/graphics/edit.png"/></a>
	<a class="deletelink" href="${h.url_for(controller='post',action='delete',id=c.post.id)}"><img src="/graphics/bin.png"/></a>
	% endif
	<div class="post_content">
		<%
		txt = h.textile(c.post.content)
		%>
		${txt|n}
	</div>
	<div class="post_meta_area">
		
	
	<div class="post_meta post_date">
		<img src="/graphics/date.png"/><span>${c.post.date.strftime("%B %d, %Y")}</span>
	</div>
	<div class="post_meta post_category">
		<img src="/graphics/cats.png"/><a href="${h.url_for(controller='category',action='show',category=c.post.category.category)}">${c.post.category.category}</a>
	</div>
	<div class="post_meta post_comments_link">
		<img src="/graphics/comments.png"/><a href="${h.url_for(controller='post',action='show',id=c.post.id)}"><span>${len(c.post.comments)} Comments</span></a>
	</div>
	
	<div class="post_meta post_keywords">
		% if len(c.post.keywords) == 0:
		Tags: None
		% else:
		<%
		keywordLinks = []
		linkStr = "<a href='%s'>%s</a>"
		for x in c.post.keywords:
			link = h.url_for(controller="tags",action="show",keyword=x.keyword)
			keywordLinks.append(linkStr%(link,x.keyword))
		%>
		Tags: ${", ".join(keywordLinks)|n}
		% endif
	</div>
	</div>
	% if not c.post_list:
	<%include file="/comment/show.mako"/>
	% endif
</div>
