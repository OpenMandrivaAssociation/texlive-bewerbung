Name:		texlive-bewerbung
Version:	61632
Release:	2
Summary:	Typesetting job applications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bewerbung
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bewerbung.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bewerbung.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bewerbung.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides packages and classes for typesetting
applications with titlepage, cover letter, cv and additional
documents in just a single document. There is also a class for
printing a table of the latest applications that can be shown
to the German authorities. The data for these applications can
be maintained in a simple CSV file.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bewerbung
%{_texmfdistdir}/tex/latex/bewerbung
%doc %{_texmfdistdir}/doc/latex/bewerbung

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
