<div class="post_comments">
	<div class="header">
		<h3><strong>heres</strong> <em>what others thought...</em></h3>
	</div>
% for cm in c.post.comments:
<div class="post_comment">
	<img height="64" src="${h.url_for(str('/gravatar/'+cm.email))}"/>
	<a href="${cm.url}"><span class="comment_author">${cm.author}</span></a>
	<span class="comment_date">${cm.date.strftime("%B %d, %Y")}</span>
	<span class="comment_content">
	<%
	txt = h.textile(cm.content)
	%>
	${txt|n}</span>
</div>
% endfor
% if len(c.post.comments) == 0:
<p> be the <strong>first</strong> to replay...</p>
% else:
<p> Interested? Why not comment...</p>
% endif
<%include file="/comment/create.mako"/>
</div>