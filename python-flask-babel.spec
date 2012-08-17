%global mod_name	Flask-Babel

Name:		python-flask-babel
Version:	0.8
Release:	1
Summary:	Adds i18n/l10n support to Flask applications
Group:		Development/Python
License:	BSD
URL:		http://github.com/mitsuhiko/flask-babel/
Source0:	http://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-babel
BuildRequires:	python-flask
BuildRequires:	python-jinja2
BuildRequires:	python-speaklater
Requires:	python-babel
Requires:	python-flask
Requires:	python-jinja2
Requires:	python-speaklater
%py_requires -d

%description
Adds i18n/l10n support to Flask applications with the help of the Babel
library.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root $RPM_BUILD_ROOT

%check
PYTHONPATH=$RPM_BUILD_ROOT/%{python_sitelib}:%{python_sitelib} make test

%files
%doc docs LICENSE PKG-INFO README
%{python_sitelib}/*-nspkg.pth
%{python_sitelib}/*.egg-info/
%{python_sitelib}/flaskext/*.py*
