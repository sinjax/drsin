
<form action="${h.url_for(controller='comment',action='create')}" class="comment_create" method="POST" accept-charset="utf-8">
	<input type="hidden" name="postid" value="${c.post.id}">
	<p><label for="author">Name:</label><br/><input type="text" name="author" value="" class="author"/></p>
	<p><label for="author">Email (used for gravatar)</label><br/><input type="text" name="email" value="" class="email"></p>
	<p><label for="author">Website (linked on name)</label><br/><input type="text" name="website" value="" class="website"></p>
	<p><label for="author">Comment (textile enabled)</label><br/><textarea name="content" class="content"></textarea></p>
	<p><input type="submit" value="Submit"></p>
</form>