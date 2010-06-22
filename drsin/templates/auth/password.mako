<%inherit file="/admin/base.mako"/>
<%def name="title()">
Change Your Password
</%def>
<%def name="header()">
</%def>
<%def name="isCurrentPage(name)"><%
current= ""
if name=="Password":
	current = "current"
%>${current}</%def>
${h.form_start(h.url_for(controller="auth",action="password_change"), method="post",id="password")}
	${h.field(
		"Current Password",
		h.password(name='current'),
	)}
	${h.field(
		"Password",
		h.password(name='newpass'),
	)}
	${h.field(
		"Retype Password",
		h.password(name='retypepass'),
	)}
	${h.field(field=h.submit(value="Change Password", name='submit'))}
${h.form_end()}