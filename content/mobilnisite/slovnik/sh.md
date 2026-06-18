---
slug: "sh"
url: "/mobilnisite/slovnik/sh/"
type: "slovnik"
title: "SH – Spherical Harmonics"
date: 2025-01-01
abbr: "SH"
fullName: "Spherical Harmonics"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sh/"
summary: "Sférické harmoniky (SH) jsou matematický rámec používaný v immersivních mediálních službách 3GPP, konkrétně pro prostorovou zvukovou složku 360stupňového a volumetrického videa. Umožňují efektivní rep"
---

SH je matematický rámec používaný v 3GPP pro prostorový zvuk v immersivních médiích, který umožňuje efektivní reprezentaci a kompresi zvukových polí pro realistický 3D audio zážitek.

## Popis

Sférické harmoniky (SH) jsou souborem ortogonálních bázových funkcí definovaných na povrchu koule. V 3GPP, konkrétně v kontextu služeb immersivních médií (např. 360stupňové video, virtuální realita a rozšířená realita), se SH využívají jako základní matematický nástroj pro reprezentaci prostorového zvuku. Prostorový zvuk si klade za cíl rekonstruovat trojrozměrné zvukové pole, což posluchači umožňuje vnímat zvuky přicházející z konkrétních směrů a vzdáleností, což je pro immersivní zážitek klíčové. Akustický tlak v bodě prostoru lze rozložit na nekonečnou řadu funkcí sférických harmonik. V praxi je tato nekonečná řada omezena na konečný řád (např. 1., 3. nebo 5. řád), což poskytuje aproximaci zvukového pole s množstvím dat, které lze efektivně zpracovat.

Proces začíná zachycením nebo syntézou zvukového pole pomocí mikrofonních polí nebo definicí zvukových objektů. Tato data zvukového pole jsou následně zakódována do koeficientů sférických harmonik. Tyto koeficienty jsou v podstatě váhy přiřazené každé bázové funkci. Vyšší řád reprezentace SH zachycuje podrobnější prostorové informace (vyšší úhlové rozlišení), ale vyžaduje více koeficientů a tím i větší šířku pásma. Například Ambisonics 1. řádu (formát založený na SH) používá 4 kanály (W, X, Y, Z), zatímco 3. řád používá 16 kanálů. Specifikace 3GPP, jako například TS 26.253 pro immersivní audio, definují, jak se tyto audio proudy založené na SH multiplexují, přenášejí a synchronizují s videem v rámci [MPEG](/mobilnisite/slovnik/mpeg/) mediálních kontejnerů, jako je [ISOBMFF](/mobilnisite/slovnik/isobmff/).

Na přijímací straně (např. ve [VR](/mobilnisite/slovnik/vr/) headsetu nebo pokročilém mediálním přehrávači) jsou koeficienty SH dekódovány. Dekodér použije koeficienty k rekonstrukci aproximace původního zvukového pole. Toto rekonstruované pole může být následně vykresleno (rendrováno) pro přehrávání na konkrétním výstupním audio zařízení posluchače, ať už se jedná o sluchátka (s využitím binauračního rendrování), stereofonní reproduktorový systém nebo plné pole pro surround sound. Pro přehrávání do sluchátek renderer aplikuje funkce přenosu hlavy ([HRTF](/mobilnisite/slovnik/hrtf/)), aby simuloval směrovost zvuků. Použití SH poskytuje formátově nezávislou mezireprezentaci; audio je uloženo a přenášeno v doméně SH a finální rendrování je přizpůsobeno prostředí přehrávání, což nabízí vysokou flexibilitu a efektivitu pro doručování immersivních médií přes mobilní sítě.

## K čemu slouží

Sférické harmoniky byly v 3GPP přijaty za účelem řešení výzvy efektivního doručování immersivního prostorového zvuku pro služby jako 360stupňové video a virtuální realita přes mobilní sítě s omezenou šířkou pásma. Tradiční kanálové audio (např. surround 5.1 nebo 7.1) je vázáno na konkrétní rozmístění reproduktorů a neadaptuje se dobře na různá prostředí přehrávání, zejména na [VR](/mobilnisite/slovnik/vr/) založené na sluchátkách. Audio založené na objektech, kde je každý zvuk objekt s metadaty, může být flexibilní, ale u složitých scén s mnoha zvuky se stává výpočetně náročným a náročným na šířku pásma.

Audio založené na SH, často realizované ve formě Ambisonics, představuje kompromisní řešení. Reprezentuje celé zvukové pole jako soubor koeficientů, což je efektivnější než přenos desítek jednotlivých zvukových objektů. Tato reprezentace je nezávislá na orientaci posluchače během kódování, což ji činí ideální pro 360stupňový obsah, kde se uživatel může rozhlížet. Hlavní motivací pro její zařazení do standardů 3GPP (počínaje Release 18) bylo vytvořit standardizovanou, interoperabilní a síťově efektivní metodu pro prostorový zvuk jako klíčovou součást kvalitního zážitku z immersivních médií, která zajistí všem uživatelům konzistentní a působivý audiovizuální zážitek bez ohledu na jejich zařízení.

## Klíčové vlastnosti

- Efektivní matematická reprezentace 3D zvukových polí
- Formátově nezávislá mezireprezentace pro prostorový zvuk
- Podpora proměnlivého řádu pro kompromis mezi kvalitou a datovým tokem
- Oddělení zachycení/přenosu od vykreslování při přehrávání
- Nativní podpora 360stupňového obsahu a rotace posluchače
- Umožňuje binaurační rendrování pro VR/AR založené na sluchátkách

## Související pojmy

- [VR – Virtualized Resource](/mobilnisite/slovnik/vr/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description

---

📖 **Anglický originál a plná specifikace:** [SH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sh/)
