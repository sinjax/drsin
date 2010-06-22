
<div id="post_${c.post.id}">
	<h2 class="post_title">
		<a href="${h.url_for(controller='post',action='show',id=c.post.id)}">${c.post.title}</a>
	</h2>
	<div class="post_date">
		${c.post.date}
	</div>
	<div class="post_keywords">
		% for x in c.post.keywords:
		${x.keyword}
		% endfor
	</div>
	<div class="post_category">
		${c.post.category.category}
	</div>
	<div class="post_comments">
		${len([x for x in c.post.comments if (x.ham/x.spam) > 1])}
	</div>
	<a href="${h.url_for(controller='post',action='show',id=c.post.id)}" title="permalink" alt="permalink"><img src="/graphics/link.png"/></a>
	<img src="/graphics/globe.png"/>
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
</div>
