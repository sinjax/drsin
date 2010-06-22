<%inherit file="/base.mako"/>
<%def name="title()">
Articles
</%def>
% if "user" in session and session["user"]:
<!-- ${session["user"].username} Logged In! -->
<script type="text/javascript" charset="utf-8">
	$(document).ready(function  (argument) {
		$(".addlink").click(function (argument) {
			$.get("${h.url_for(controller='post',action='create')}",function (data) {
				$("#addarea").html(data)
			})
			return false;
		})
	})
</script>
<div id="addarea">
	<a class="addlink" href="${h.url_for(controller='post',action='create')}"><img src="/graphics/add.png"/></a>
</div>


% endif
% for p in c.posts:
	<%
		c.post = p
	%>
	<%include file="/post/post.mako"/>
% endfor