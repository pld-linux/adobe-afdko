%global archivename afdko
%global antl4_ver 4.9.3

Summary:	Adobe Font Development Kit for OpenType
Name:		adobe-afdko
Version:	4.0.1
Release:	1
# ExternalAntlr4Cpp.cmake is BSD-3-clause
# c/makeotf/makeotf_lib/build/hotpccts/pccts/* is ANTLR-PD
# afdko-3.6.1/python/afdko/pdflib/pdfgen.py is Python-2.0.1
# python/afdko/resources/ is BSD-3-Clause
License:	Apache-2.0 AND BSD-3-Clause AND ANTLR-PD AND Python-2.0.1
URL:		https://github.com/adobe-type-tools/afdko
Source0:	https://github.com/adobe-type-tools/%{archivename}/releases/download/%{version}/%{archivename}-%{version}.tar.gz
# Source0-md5:	2a3ba9bb2583be0d744220411a8f24f1
Source1:	https://www.antlr.org/download/antlr4-cpp-runtime-%{antl4_ver}-source.zip
# Source1-md5:	eafa4fef583e12e963062882773461be
Patch0:		antlr4-cpp-runtime-%{antl4_ver}.patch
BuildRequires:	cmake
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel
BuildRequires:	utf8cpp-devel

%description
Adobe Font Development Kit for OpenType (AFDKO). The AFDKO is a set of
tools for building OpenType font files from PostScript and TrueType
font data.

%prep
%setup -q -n %{archivename}-%{version}
%patch -P0 -p1

cp %{SOURCE1} .

%build
install -d build
cd build
%{cmake} ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/ README.md NEWS.md LICENSE.md
%attr(755,root,root) %{_bindir}/detype1
%attr(755,root,root) %{_bindir}/makeotfexe
%attr(755,root,root) %{_bindir}/mergefonts
%attr(755,root,root) %{_bindir}/rotatefont
%attr(755,root,root) %{_bindir}/sfntdiff
%attr(755,root,root) %{_bindir}/sfntedit
%attr(755,root,root) %{_bindir}/spot
%attr(755,root,root) %{_bindir}/tx
%attr(755,root,root) %{_bindir}/type1

