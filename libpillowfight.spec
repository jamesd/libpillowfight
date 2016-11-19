Name:           libpillowfight
Version:        0.2.1
Release:        1%{?dist}
Summary:        Small library containing various image processing algorithms

License:        gplv2
URL:            https://github.com/jflesch/%{name}
Source0:        https://github.com/jflesch/%{name}/archive/%{version}/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-pillow-devel

%description
Library containing various image processing algorithms. It includes
Python 3 bindings designed to operate on Pillow images (PIL.Image).

The C library depends only on the libc. The Python bindings depend
only on Pillow.

APIs are designed to be as simple to use as possible. Default values
are provided for every parameters.

%package -n libpillowfight-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:	libpillowfight

%description -n libpillowfight-devel
%{description}


%package -n python3-pillowfight
Summary:        %{summary}
Requires:	python3-pillow

%description -n python3-pillowfight
%{description}


%prep
%setup -q


%build
%cmake .
make %{?_smp_mflags}
%{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=%{buildroot}
%if %{_arch} == "x86_64"
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f


# %check
# %{__python3} setup.py test


%files
%license LICENSE
%doc README.md ChangeLog
%{_libdir}/%{name}.so

%files -n libpillowfight-devel
%license LICENSE
%{_includedir}/

%files -n python3-pillowfight
%license LICENSE
%{python3_sitearch}/*


%changelog
* Sat Nov 19 2016 James Davidson <james@greycastle.net> - 0.2.1-1
- Initial packaging

