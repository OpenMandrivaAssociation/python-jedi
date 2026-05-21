%define module jedi
%bcond tests 1

Name:		python-jedi
Version:	0.20.0
Release:	1
Summary:	An auto completion tool for Python
Group:		Development/Python
License:	MIT
URL:		https://jedi.readthedocs.io
# upstream  https://github.com/davidhalter/jedi
Source0:	https://files.pythonhosted.org/packages/source/j/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	fdupes
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(parso)
%endif

%description
Jedi is a static analysis tool for Python that is typically used in
IDEs/editors plugins.

Jedi has a focus on autocompletion and goto functionality.
Other features include refactoring, code search and finding references

Jedi uses a very simple interface to connect with IDE's. As an reference,
there is a VIM implementation, which uses Jedi's auto completion. However,
I encourage you to use Jedi in your IDEs. Start writing plugins! If there are
problems with licensing, just contact me.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%install -a
# package installs a load of zero-length files from third party typshed/stubs
find %{buildroot} -type f -empty -delete
# package has a lot of duplicated files, fix it with fdupes
%fdupes %{buildroot}%{python_sitelib}/%{module}

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
skiptests="not test_venv_and_pths"
skiptests+=" and not test_find_system_environments"
skiptests+=" and not test_import"
skiptests+=" and not test_create_environment_venv_path"
skiptests+=" and not test_changing_venv"
skiptests+=" and not test_working_venv"
skiptests+=" and not test_scanning_venvs"
pytest -rs -k "$skiptests"
%endif

%files
%doc README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
