#
# Conditional build:
%bcond_with	tests	# unit tests (many failures)

Summary:	Plugin for nose or pytest that automatically reruns flaky tests
Summary(pl.UTF-8):	Wtyczka dla nose lub pytesta automatycznie uruchamiająca ponownie niepewne testy
Name:		python3-flaky
Version:	3.8.1
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/flaky/
Source0:	https://files.pythonhosted.org/packages/source/f/flaky/flaky-%{version}.tar.gz
# Source0-md5:	59d67ca4439d37936fb7368c140d23e7
URL:		https://pypi.org/project/flaky/
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-genty
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flaky is a plugin for nose or pytest that automatically reruns flaky
tests.

Ideally, tests reliably pass or fail, but sometimes test fixtures must
rely on components that aren't 100% reliable. With flaky, instead of
removing those tests or marking them to @skip, they can be
automatically retried.

%description -l pl.UTF-8
Flaky to wtyczka dla nose lub pytesta automatycznie uruchamiająca
ponownie niepewne testy.

Idealnie testy powinny deterministycznie powodzić się lub nie, ale
czasem wypozażenia testów muszą polegać na komponentach nie w pełni
deterministycznych. Przy pomocy modułu flaky, zamiast usuwania tych
testów lub oznaczania ich @skip, można je automatycznie ponowić.

%prep
%setup -q -n flaky-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/flaky
%{py3_sitescriptdir}/flaky-%{version}-py*.egg-info
