---
slug: "br"
url: "/mobilnisite/slovnik/br/"
type: "slovnik"
title: "BR – Bandwidth Reduced"
date: 2025-01-01
abbr: "BR"
fullName: "Bandwidth Reduced"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/br/"
summary: "Bandwidth Reduced (BR) označuje přenosové režimy a kategorie UE navržené pro provoz s užšími kanálovými šířkami pásma než standardní konfigurace LTE/NR. Umožňuje cenově výhodné implementace zařízení a"
---

BR je 3GPP termín pro přenosové režimy a kategorie UE navržené pro provoz s užšími kanálovými šířkami pásma než standardní LTE/NR, aby umožnily cenově výhodná zařízení a podporovaly IoT aplikace jako LTE-M a NB-IoT.

## Popis

Bandwidth Reduced (BR) je základní koncept ve standardech 3GPP, který definuje přenosové režimy a schopnosti UE optimalizované pro provoz s výrazně sníženými kanálovými šířkami pásma ve srovnání s konvenčními buněčnými systémy. V LTE se standardní kanálové šířky pohybují od 1,4 MHz do 20 MHz, zatímco BR konfigurace typicky pracují s 1,4 MHz nebo ještě užšími šířkami pásma (200 kHz pro NB-IoT). Toto snížení šířky pásma přímo ovlivňuje návrh fyzické vrstvy, což vyžaduje úpravy synchronizačních signálů, referenčních signálů, řídicích kanálů a datových kanálů, aby byla zachována spolehlivá funkce v omezeném spektru.

Architektura BR systémů zahrnuje specializované kategorie UE (kategorie M pro LTE-M, kategorie [NB](/mobilnisite/slovnik/nb/) pro NB-IoT), které implementují zjednodušené řetězce RF a základního pásma. Tato UE podporují snížené špičkové datové rychlosti, omezené stavy mobility a funkce šetřící energii, jako je rozšíšené nespojité příjímání (eDRX) a režim úspory energie (PSM). Na straně sítě jsou vyžadovány odpovídající vylepšení pro podporu těchto UE, včetně upravených procedur náhodného přístupu, mechanismů pagingu a protokolů správy spojení, které berou v úvahu omezené schopnosti BR zařízení.

Z pohledu protokolů ovlivňuje BR provoz více vrstev protokolového zásobníku. Na fyzické vrstvě (specifikované v 36.321 a 36.331) zavádí BR nové velikosti transportních bloků, upravené modulační schémata (primárně QPSK pro řídicí kanály) a zjednodušené kódování kanálu. Na [MAC](/mobilnisite/slovnik/mac/) vrstvě implementují BR UE snížené velikosti vyrovnávací paměti a upravené mechanismy plánování. [RRC](/mobilnisite/slovnik/rrc/) vrstva zahrnuje specifické procedury pro indikaci a konfiguraci schopností BR UE, což síti umožňuje přizpůsobit své chování na základě omezených schopností UE.

Role BR v síti přesahuje pouhé snížení šířky pásma. Umožňuje síťovým operátorům nasazovat IoT služby pomocí stávající infrastruktury LTE s minimálními úpravami, čímž vytváří cenově efektivní cestu k masivnímu nasazení IoT. BR zařízení mohou koexistovat s běžnými LTE zařízeními ve stejném spektru prostřednictvím pečlivé alokace zdrojů a řízení interference. Síť spravuje BR zařízení pomocí vyhrazených systémových informačních bloků, specifických RRC zpráv a upravených procedur mobility, které zohledňují jejich omezené měřicí schopnosti a snížené požadavky na mobilitu.

## K čemu slouží

Technologie Bandwidth Reduced byla vytvořena, aby řešila specifické požadavky komunikace typu stroj-stroj a IoT aplikací, které se zásadně liší od služeb mobilního širokopásmového připojení orientovaných na člověka. Tradiční LTE zařízení byla navržena pro vysoké datové rychlosti, nepřetržité připojení a složité scénáře mobility – vlastnosti, které jsou pro mnoho IoT aplikací, jako jsou chytré měřiče, sledování majetku a environmentální senzory, zbytečné a cenově neúnosné. Vysoká složitost a spotřeba energie standardních LTE UE je činila nevhodnými pro IoT zařízení napájená bateriemi s požadavky na životnost baterie v řádu desetiletí.

Historicky, předtím než 3GPP standardizovalo BR technologie, se IoT řešení spoléhala na proprietární protokoly nebo sítě 2G, které nabízely omezenou škálovatelnost, zabezpečení a kvalitu služeb. Zavedení BR ve vydání 13 (LTE-M a NB-IoT) poskytlo standardizovaný, na buněčných sítích založený přístup k masivnímu nasazení IoT. Tím se odstranila omezení předchozích přístupů díky nabídnutí lepšího pokrytí (prostřednictvím opakování a zvýšení výkonu), lepšího zabezpečení (převzatého z LTE) a bezproblémové integrace se stávajícími mobilními sítěmi.

Motivace pro BR přesahuje pouhé snížení nákladů. Minimalizací požadavků na šířku pásma umožňuje BR efektivnější využití spektra pro IoT provoz, což operátorům umožňuje podporovat obrovské množství zařízení bez nutnosti vyčleňovat velké části svého spektra. Také usnadňuje globální roaming prostřednictvím standardizovaných specifikací a umožňuje nové obchodní modely pro nízkonákladová, nízkopříkonová připojená zařízení. Vývoj BR v následujících vydáních dále optimalizoval tyto aspekty při zachování zpětné kompatibility s dřívějšími BR UE.

## Klíčové vlastnosti

- Provoz s kanálovou šířkou pásma 1,4 MHz nebo užší
- Podpora pro snížené kategorie UE (Cat-M, Cat-NB) se zjednodušenými RF řetězci
- Vylepšené pokrytí prostřednictvím technik opakování a zvýšení výkonu
- Funkce šetřící energii včetně eDRX a režimu úspory energie (PSM)
- Koexistence s běžnými LTE UE ve stejném spektru
- Upravené kanály a procedury fyzické vrstvy pro úzkopásmový provoz

## Definující specifikace

- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [BR na 3GPP Explorer](https://3gpp-explorer.com/glossary/br/)
