<%
formOptions = {
	"class":"comment_create",
	"name":"comment"
}
%>
<%def name="formError(part)">
% if part in c.form_errors :
<span class="form_error">${c.form_errors[part]}</span>
%endif
</%def>
<%
if not c.form_result:
	c.form_result = {}
%>
<p>comments switched <strong>off</strong> 'til I sort out the spam filter</p>
<%doc>
${h.form(h.url_for(controller="comment",action="create"),**formOptions)}
	${h.hidden("postid",value=c.post.id)}
	<p>
		<label for="author">Name:</label>${formError("author") }<br/
		<%
		opt = {
			"class":"author","value":c.form_result.get("author","")
		}
		%>
		${h.text("author",**opt)}
	</p>
	<p>
		<label for="email">Email (used for gravatar)</label>${formError("email")}<br/>
		<%
		opt = {"class":"email","value":c.form_result.get("email","")}
		%>
		${h.text("email",**opt)}
	</p>
	<p>
		<label for="website">Website (linked on name)</label>${formError("website")}<br/>
		<%
		opt = {"class":"website","value":c.form_result.get("website","")}
		%>
		${h.text("website",**opt)}
	</p>
	<p>
		<label for="content">Comment (textile enabled)</label>${formError("content")}<br/>
		<%
		opt = {"class":"content"}
		%>
		${h.textarea("content",c.form_result.get("content",""),**opt)}
	</p>
	<p><input type="submit" value="Submit"></p>
${h.end_form()}
</%doc>