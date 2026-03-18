%define module flask-babel
%define oname flask_babel
%bcond tests 1
%bcond docs 1

Name:		python-flask-babel
Version:	4.1.0
Release:	1
Summary:	Adds i18n/l10n support to Flask applications
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/python-babel/flask-babel
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
# For patch into see this PR: https://github.com/python-babel/flask-babel/pull/242
Patch0:		00-fix-list-translations-ordering-in-tests.patch

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(babel)
BuildRequires:	python%{pyver}dist(flask)
BuildRequires:	python%{pyver}dist(jinja2)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(pytz)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-mock)
%endif
%if %{with docs}
BuildRequires:	make
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(furo)
%endif

%description
Adds i18n/l10n support to Flask applications with the help of the Babel library.

%if %{with docs}
%build -a
make -C docs html
rm -rf docs/_build/html/.buildinfo
%endif

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif


%files
%if %{with docs}
%doc docs/_build/html README.md
%else
%doc README.md
%endif
%license LICENSE
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
