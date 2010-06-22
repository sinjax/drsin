<script type="text/javascript" charset="utf-8">
<%
editingID = "add"
if c.post.id:
	editingID = c.post.id

%>
function submit_post_${editingID}() {
	% if c.post.id:
	$.post("${h.url_for(controller='post',action='update')}", 
	% else:
	$.post("${h.url_for(controller='post',action='create')}",
	% endif
			$("#edit_${editingID}").serialize(),
			function (msg) {
				% if c.post.id:
				$.get("${h.url_for(controller='post',action='show',id=c.post.id,isolated=True)}",function  (data) {
					$("#post_${c.post.id}").html(data)
					return false;
				})
				% else:
				location.href = "${h.url_for('/')}"
				% endif
				return false;
			}
		);
	return false
}
$.get("${h.url_for('/categories')}",function (data) {
	data = data.split(",")
	$(".category").autocomplete(data);
});
$.get("${h.url_for('/keywords')}",function (data) {
	data = data.split(",")
	$(".keywords").autocomplete(data,{
		multiple: true
	});
});

</script>

<form class="edit" id="edit_${editingID}" method="POST" accept-charset="utf-8">
	<%
	keywordStr = ""
	if c.post != None and c.post.keywords != None: keywordStr = ", ".join([k.keyword for k in c.post.keywords])
	catStr = ""
	if c.post != None and c.post.category != None: catStr = c.post.category.category
	%>
	<p><input type="hidden" name="id" value="${c.post.id}" class="id"></p>
	<p><input type="text" name="title" value="${c.post.title}" class="title"/></p>
	<p><input type="text" name="category" value="${catStr}" class="category"></p>
	<p><input type="text" name="keywords" value="${keywordStr}" class="keywords"></p>
	<p><textarea name="content" class="content">${c.post.content}</textarea></p>
	<p><input type="submit" value="Submit" onclick="return submit_post_${editingID}();"></p>
</form>