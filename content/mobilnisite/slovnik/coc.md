---
slug: "coc"
url: "/mobilnisite/slovnik/coc/"
type: "slovnik"
title: "COC – Cell Outage Compensation"
date: 2025-01-01
abbr: "COC"
fullName: "Cell Outage Compensation"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/coc/"
summary: "Cell Outage Compensation (COC) je samoléčebný mechanismus v mobilních sítích, který automaticky detekuje výpadky buněk a upravuje parametry sousedních buněk, aby zachoval pokrytí službou a kapacitu. M"
---

COC je samoléčebný mechanismus, který automaticky detekuje výpadky buněk a upravuje parametry sousedních buněk za účelem zachování pokrytí službou a kapacity během výpadku.

## Popis

Cell Outage Compensation (COC) je klíčová funkce samoorganizující se sítě (SON) v rámci systému správy, provozu a údržby (OAM) sítí 3GPP. Funguje jako automatizační mechanismus s uzavřenou smyčkou, který detekuje, kdy se základnová stanice nebo buňka stane nedostupnou kvůli hardwarové poruše, softwarovým problémům, ztrátě napájení nebo údržbovým činnostem. Po detekci COC zahájí kompenzační proceduru, při které jsou sousední buňky rekonfigurovány tak, aby rozšířily své oblasti pokrytí a absorbovaly provozní zatížení z porouchané buňky. To zahrnuje sofistikované algoritmy, které vypočítávají optimální úpravy parametrů pro více buněk současně, přičemž se vyhýbají rušení a zachovávají celkovou stabilitu sítě.

Architektura COC je rozdělena mezi systém správy sítě ([NMS](/mobilnisite/slovnik/nms/)) a základnové stanice, přičemž NMS typicky hostí centrální funkci COC, která koordinuje kompenzaci napříč více buňkami. Mezi klíčové komponenty patří modul detekce výpadku, který využívá hlášení o výkonu, oznámení alarmů a kontroly konektivity; jádro kompenzačního algoritmu, které vypočítává úpravy parametrů; a rozhraní pro správu konfigurace, které aplikuje změny na živé síťové prvky. Systém při určování kompenzačních strategií zohledňuje více omezení včetně maximálních přípustných změn parametrů, prahů rušení, požadavků na kvalitu služby a limitů kapacity sítě.

COC funguje prostřednictvím vícefázového procesu: detekce, analýza, kompenzace a monitorování. Během detekce systém identifikuje podmínky výpadku pomocí ukazatelů ztráty konektivity a hlášení o degradaci výkonu. Fáze analýzy vyhodnotí oblast dopadu, identifikuje postižené uživatelské zařízení (UE) a vybere kandidátní kompenzační buňky na základě geografické sousednosti a dostupné kapacity. Kompenzace zahrnuje výpočet a aplikaci úprav parametrů, jako je zvýšení vysílacího výkonu, úprava elektrického nebo mechanického náklonu antény, změna prahových hodnot pro předání spojení a optimalizace individuálních offsetů buňky. Monitorovací fáze sleduje účinnost kompenzace prostřednictvím klíčových ukazatelů výkonu, jako jsou díry v pokrytí, spadlá hovory a metriky propustnosti, a v případě potřeby provádí další úpravy.

V praktické implementaci musí COC vyvážit účinnost kompenzace se stabilitou sítě. Systém používá postupné úpravy parametrů, aby se předešlo náhlým dopadům na celou síť, a před aplikací změn využívá simulační analýzu typu „co kdyby“. Pokročilé implementace COC zohledňují časové vzorce, předpovídají délku trvání výpadku a podle toho přizpůsobují kompenzační strategie. Technologie se integruje s dalšími funkcemi SON, jako je vyrovnávání zatížení mobility (MLB) a optimalizace robustnosti mobility ([MRO](/mobilnisite/slovnik/mro/)), aby zajistila koordinovanou optimalizaci sítě. Role COC přesahuje rámec okamžité reakce na výpadek a zahrnuje proaktivní plánování kompenzace a historickou analýzu vzorců výpadků pro zlepšení sítě.

## K čemu slouží

Cell Outage Compensation byl vytvořen, aby řešil významné narušení služeb způsobené výpadky buněk v stále hustších a složitějších mobilních sítích. Před implementací COC operátoři sítí spoléhali při výpadcích buněk na manuální odstraňování problémů a úpravu parametrů, což vedlo k dlouhodobé degradaci služeb trvající hodiny nebo dokonce dny. Tento manuální přístup byl neefektivní, náchylný k chybám a nedokázal držet krok s rostoucím počtem síťových prvků v nasazeních 3G a 4G. Rostoucí automatizace síťových operací prostřednictvím SON vytvořila základ pro automatizovanou reakci na výpadky.

Primární motivací pro vývoj COC bylo zlepšit dostupnost sítě a kvalitu uživatelského zážitku pro účastníky během neočekávaných poruch. Tradiční síťové návrhy sice zahrnovaly redundanci a překryvy, ale bez inteligentních kompenzačních mechanismů nevyhnutelně docházelo během výpadků k děrám v pokrytí a nedostatkům kapacity. COC to řeší automatickou rekonfigurací sousedních buněk za účelem zaplnění mezer v pokrytí a přerozdělení provozního zatížení. To je obzvláště důležité v městském prostředí, kde je hustota buněk vysoká a očekávání služeb přísná, stejně jako ve venkovských oblastech, kde jsou rozestupy buněk větší a mezery v pokrytí významnější.

COC řeší několik konkrétních omezení předchozích přístupů: snižuje střední dobu do opravy (MTTR) automatizací kompenzačního procesu, minimalizuje potřebu nákladných testů jízdou pro identifikaci děr v pokrytí a předchází kaskádovým selháním, která by mohla nastat v důsledku nevhodných manuálních úprav. Tato technologie také podporuje provozní efektivitu tím, že snižuje potřebu nepřetržitého personálního obsazení operačního centra sítě pro okamžitou reakci na výpadky. Jak se sítě vyvíjely směrem k 5G se zvýšenou heterogenitou a požadavky na síťové slicing, stala se COC nezbytnou pro udržení smluv o úrovni služeb napříč různými síťovými slicy i přes výpadky jednotlivých buněk.

## Klíčové vlastnosti

- Automatická detekce výpadků buněk prostřednictvím měření výkonu a korelace alarmů
- Dynamická úprava parametrů sousedních buněk včetně výkonu, náklonu a nastavení předávání spojení
- Koordinace více buněk za účelem vyhnutí se rušení a zachování stability sítě během kompenzace
- Integrace s dalšími funkcemi SON pro komplexní optimalizaci sítě
- Podpora jak okamžité kompenzace, tak proaktivních strategií zmírňování výpadků
- Správa konfigurace s možností návratu v případě selhání kompenzace

## Definující specifikace

- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 32.522** (Rel-11) — SON Policy NRM IRP Information Service

---

📖 **Anglický originál a plná specifikace:** [COC na 3GPP Explorer](https://3gpp-explorer.com/glossary/coc/)
