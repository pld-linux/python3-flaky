#
# Conditional build:
%bcond_with	tests	# unit tests (many failures)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Plugin for nose or pytest that automatically reruns flaky tests
Summary(pl.UTF-8):	Wtyczka dla nose lub pytesta automatycznie uruchamiająca ponownie niepewne testy
Name:		python-flaky
Version:	3.6.1
Release:	6
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/flaky/
Source0:	https://files.pythonhosted.org/packages/source/f/flaky/flaky-%{version}.tar.gz
# Source0-md5:	7427c11cd74e8851f1d7bf2690b646b5
Patch0:		%{name}-mock.patch
URL:		https://pypi.org/project/flaky/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-genty
BuildRequires:	python-mock
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-genty
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
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

%package -n python3-flaky
Summary:	Plugin for nose or pytest that automatically reruns flaky tests
Summary(pl.UTF-8):	Wtyczka dla nose lub pytesta automatycznie uruchamiająca ponownie niepewne testy
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-flaky
Flaky is a plugin for nose or pytest that automatically reruns flaky
tests.

Ideally, tests reliably pass or fail, but sometimes test fixtures must
rely on components that aren't 100% reliable. With flaky, instead of
removing those tests or marking them to @skip, they can be
automatically retried.

%description -n python3-flaky -l pl.UTF-8
Flaky to wtyczka dla nose lub pytesta automatycznie uruchamiająca
ponownie niepewne testy.

Idealnie testy powinny deterministycznie powodzić się lub nie, ale
czasem wypozażenia testów muszą polegać na komponentach nie w pełni
deterministycznych. Przy pomocy modułu flaky, zamiast usuwania tych
testów lub oznaczania ich @skip, można je automatycznie ponowić.

%prep
%setup -q -n flaky-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
LC_ALL=C.UTF-8 \
%{__python} -m unittest discover -s test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/flaky
%{py_sitescriptdir}/flaky-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-flaky
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/flaky
%{py3_sitescriptdir}/flaky-%{version}-py*.egg-info
%endif
