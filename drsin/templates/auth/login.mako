<%inherit file="/base.mako"/>
${h.form_start(h.url_for(controller="auth",action="enter"), method="post")}
    ${h.field(
        "Username",
        h.text(name='username'),
    )}
    ${h.field(
        "Password",
        h.password(name='password'),
    )}
    ${h.field(field=h.submit(value="Sign in", name='submit'))}
${h.form_end()}