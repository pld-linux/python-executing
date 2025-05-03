#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Get the currently executing AST node of a frame, and other information
Summary(pl.UTF-8):	Pobieranie aktualnie wykonywanego węzła AST ramki oraz innych informacji
Name:		python-executing
# keep 1.x here for python2 support
Version:	1.2.0
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/executing/
Source0:	https://files.pythonhosted.org/packages/source/e/executing/executing-%{version}.tar.gz
# Source0-md5:	e6fa9a6abf00555ccc8a6b3524729238
URL:		https://pypi.org/project/executing/
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
BuildRequires:	python-toml
%if %{with tests}
BuildRequires:	python-asttokens
BuildRequires:	python-littleutils
BuildRequires:	python-pytest
BuildRequires:	python-typing
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This mini-package lets you get information about what a frame is
currently doing, particularly the AST node being executed.

%description -l pl.UTF-8
Ten minipakiet pozwala pobierać informacje o wykonywanej aktualnie
ramce, w szczególności węźle AST.

%prep
%setup -q -n executing-%{version}

%build
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%{py_sitescriptdir}/executing
%{py_sitescriptdir}/executing-%{version}-py*.egg-info
