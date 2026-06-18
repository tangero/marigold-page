---
slug: "svn"
url: "/mobilnisite/slovnik/svn/"
type: "slovnik"
title: "SVN – Satellite Virtual Network"
date: 2025-01-01
abbr: "SVN"
fullName: "Satellite Virtual Network"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/svn/"
summary: "Logická síťová abstrakce, která umožňuje satelitním přístupovým sítím integrovat se se sítěmi jádra 3GPP, což uživatelskému zařízení (UE) umožňuje přístup ke službám přes satelitní spoje. Poskytuje sp"
---

SVN je logická síťová abstrakce, která umožňuje satelitním přístupovým sítím integrovat se se sítěmi jádra 3GPP, čímž rozšiřuje pozemní mobilní pokrytí a služby do odlehlých oblastí prostřednictvím satelitních spojů.

## Popis

Satellite Virtual Network (SVN) je koncept architektury sítě jádra v rámci 3GPP, který usnadňuje integraci satelitních rádiových přístupových sítí se standardizovanou sítí jádra 3GPP. Je definován jako logická síťová entita, která prezentuje satelitní přístupovou síť jádru tak, jako by šlo o pozemní přístupovou síť, a abstrahuje specifické charakteristiky satelitního spoje. SVN zajišťuje funkce jako správu mobility, správu relací a propojení s domovskou veřejnou pozemní mobilní sítí ([HPLMN](/mobilnisite/slovnik/hplmn/)) nebo navštívenou veřejnou pozemní mobilní sítí ([VPLMN](/mobilnisite/slovnik/vplmn/)), což uživatelskému zařízení (UE) umožňuje registraci, autentizaci a navázání datových relací přes satelitní spojení.

Z architektonického hlediska se SVN rozhraními standardizovanými v 3GPP (např. [S1-MME](/mobilnisite/slovnik/s1-mme/), [N2](/mobilnisite/slovnik/n2/)) propojuje s uzly sítě jádra 3GPP, jako je Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G. Může zahrnovat specifické adaptace pro vyrovnání se s dlouhými přenosovými zpožděními, přerušovanou konektivitou a odlišnými protokoly linkové vrstvy, které jsou vlastní satelitní komunikaci. Mezi klíčové komponenty v rámci SVN patří virtualizované síťové funkce, které emulují pozemní řadiče základnových stanic nebo brány přístupové sítě, spolu s potřebnými převodníky protokolů a vyrovnávacími paměťmi pro správu časování a signalizačních rozdílů. SVN funguje jako most, který překládá mezi satelitně specifickými rádiovými protokoly a protokoly sítě jádra 3GPP.

Princip fungování: Když se UE pokusí připojit přes satelit, satelitní přístupová síť přepošle požadavek na připojení do SVN. SVN tento požadavek zpracuje a pro autentizaci a autorizaci komunikuje s entitami sítě jádra (např. přes [HSS](/mobilnisite/slovnik/hss/)/[UDM](/mobilnisite/slovnik/udm/)). Vytvoří pro UE kontext virtuálního spojení a spravuje nastavení přenosového kanálu (bearer) nebo PDU relace. Po celou dobu relace SVN zpracovává události mobility (jako je předávání mezi satelity) a spravuje kvalitu služeb, případně aplikuje optimalizace pro spoje s vysokou latencí. Jeho role je klíčová pro zajištění plynulé kontinuity služeb a rozšíření služeb založených na 3GPP – hlasových, datových a IoT – na námořní, letecké a geograficky izolované regiony, kde není dostupná pozemní infrastruktura.

## K čemu slouží

Koncept SVN byl vytvořen, aby řešil výzvu poskytnutí všudypřítomného pokrytí službami 3GPP, a to i v oblastech, kde je nasazení pozemní mobilní infrastruktury ekonomicky nebo fyzicky neproveditelné, jako jsou oceány, pouště a polární regiony. Před jeho standardizací satelitní komunikační systémy často fungovaly jako samostatné, neintegrované sítě, což vyžadovalo dvou režimová zařízení a komplexní řešení pro vzájemné propojení, aby uživatelé mohli využívat jak mobilní, tak satelitní služby. Toto rozdělení omezovalo plynulou mobilitu a kontinuitu služeb.

Zaveden v 3GPP Release 5, byl SVN součástí širšího úsilí o definici vzájemného propojení sítí a podpory pro přístupy nezávislé na 3GPP. Řeší problém integrace satelitního přístupu do ekosystému 3GPP tím, že poskytuje standardizovanou vrstvu virtuální sítě, která skrývá specifické složitosti satelitní komunikace před sítí jádra. To umožňuje operátorům využívat satelitní sítě k rozšíření pokrytí bez nutnosti rozsáhlých úprav protokolů a procedur sítě jádra. Motivací byly regulatorní požadavky na nouzovou komunikaci, potřeby námořního a leteckého průmyslu a cíl dosáhnout skutečně globální konektivity pro budoucí mobilní služby, včetně 5G a dalších generací.

## Klíčové vlastnosti

- Logická abstraktní vrstva integrující satelitní přístup se sítí jádra 3GPP
- Podpora správy mobility a správy relací přes satelitní spoje
- Adaptace na vysoká přenosová zpoždění a přerušovanou satelitní konektivitu
- Spolupráce s HSS/UDM pro autentizaci účastníka a načítání profilů
- Standardizovaná rozhraní (např. založená na 24.229) k řídicím funkcím sítě jádra
- Umožňuje kontinuitu služeb a roaming mezi pozemními a satelitními sítěmi

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP

---

📖 **Anglický originál a plná specifikace:** [SVN na 3GPP Explorer](https://3gpp-explorer.com/glossary/svn/)
