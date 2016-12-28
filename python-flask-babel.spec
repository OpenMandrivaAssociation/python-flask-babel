%global mod_name	Flask-Babel

Name:		python-flask-babel
Version:	0.9
Release:	3
Summary:	Adds i18n/l10n support to Flask applications

Group:		Development/Python
License:	BSD
URL:		http://github.com/mitsuhiko/flask-babel/
Source0:	http://pypi.python.org/packages/source/F/Flask-Babel/Flask-Babel-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-babel
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	python-flask
BuildRequires:	python-jinja2
BuildRequires:  python-pytz
BuildRequires:	python-speaklater

BuildRequires:	python2-babel
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-flask
BuildRequires:  python2-jinja2
BuildRequires:  python2-pytz
BuildRequires:  python2-speaklater

Requires:	python-babel
Requires:	python-flask
Requires:	python-jinja2
Requires:   python-pytz
Requires:	python-speaklater


%description
Adds i18n/l10n support to Flask applications with the help of the Babel
library.

%prep
%setup -q -n %{mod_name}-%{version}

%build
python setup.py build

%install
python setup.py install --root %{buildroot}

# Disable tests - date-related tests may fail inside build nodes
# %check
# PYTHONPATH=$RPM_BUILD_ROOT/%{python_sitelib}:%{python_sitelib} make test

%files
%doc docs LICENSE PKG-INFO README
%{py_puresitedir}/*.egg-info/
%{py_puresitedir}/flask_babel


