%global mod_name	Flask-Babel
%bcond_with python2
Name:		python-flask-babel
Version:	2.0.0
Release:	1
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

%if %{with python2}
BuildRequires:	python2-babel
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-flask
BuildRequires:  python2-jinja2
BuildRequires:  python2-pytz
BuildRequires:  python2-speaklater
%endif

Requires:	python-babel
Requires:	python-flask
Requires:	python-jinja2
Requires:   	python-pytz
Requires:	python-speaklater


%description
Adds i18n/l10n support to Flask applications with the help of the Babel
library.

%if %{with python2}
%package -n python2-flask-babel
Summary:	Adds i18n/l10n support to Flask applications

%description -n python2-flask-babel
Adds i18n/l10n support to Flask applications with the help of the Babel
library.
%endif

%prep
%setup -q -n %{mod_name}-%{version}

%if %{with python2}
cp -a . %py2dir
%endif

%build
python setup.py build

%if %{with python2}
pushd %py2dir
python2 setup.py build
%endif

%install
python setup.py install --root %{buildroot}

%if %{with python2}
pushd %py2dir
python2 setup.py install --root %{buildroot}
%endif

# Disable tests - date-related tests may fail inside build nodes
# %check
# PYTHONPATH=$RPM_BUILD_ROOT/%{python_sitelib}:%{python_sitelib} make test

%files
%doc docs LICENSE PKG-INFO README.md
%{py_puresitedir}/*.egg-info/
%{py_puresitedir}/flask_babel

%if %{with python2}
%files -n python2-flask-babel
%doc docs LICENSE PKG-INFO README
%{py2_puresitedir}/*.egg-info/
%{py2_puresitedir}/flask_babel
%endif

