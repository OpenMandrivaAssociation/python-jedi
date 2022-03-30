%define module	jedi

Name:		python-%{module}
Version:	0.18.0
Release:	%mkrel 4
Summary:	An auto completion tool for Python that can be used for text editors
Group:		Development/Python
License:	LGPLv3
URL:		https://jedi.readthedocs.org/en/latest/index.html
Source0:	%{pypi_source %{module}}
BuildArch:	noarch

%description
Jedi is an auto completion tool for Python. It works. With and without
syntax errors. Sometimes it sucks, but that's normal in dynamic languages.
But it sucks less than other tools. It understands almost all of the basic
Python syntax elements including many built-ins.

Jedi uses a very simple interface to connect with IDE's. As an reference,
there is a VIM implementation, which uses Jedi's auto completion. However,
I encourage you to use Jedi in your IDEs. Start writing plugins! If there are
problems with licensing, just contact me.

%package -n	python3-%{module}
Summary:	An auto completion tool for Python 3 that can be used for text editors
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

%description -n	python3-%{module}
Jedi is an auto completion tool for Python 3. It works. With and without
syntax errors. Sometimes it sucks, but that's normal in dynamic languages.
But it sucks less than other tools. It understands almost all of the basic
Python syntax elements including many built-ins.

Jedi uses a very simple interface to connect with IDE's. As an reference,
there is a VIM implementation, which uses Jedi's auto completion. However,
I encourage you to use Jedi in your IDEs. Start writing plugins! If there are
problems with licensing, just contact me.

%prep
%setup -q -n %{module}-%{version}
%autopatch -p1

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}-py%{python3_version}.egg-info
