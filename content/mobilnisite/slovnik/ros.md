---
slug: "ros"
url: "/mobilnisite/slovnik/ros/"
type: "slovnik"
title: "ROS – Remote Operations Service"
date: 2025-01-01
abbr: "ROS"
fullName: "Remote Operations Service"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ros/"
summary: "Prvek ve vrstvě služeb CAMEL (Customised Applications for Mobile network Enhanced Logic) a IP Multimedia Subsystem (IMS), který umožňuje provádění operací na vzdálené síťové entitě. Poskytuje struktur"
---

ROS je prvek služeb CAMEL a IMS, který poskytuje strukturovaný rámec pro provádění operací, jako je správa dat účastníka a řízení služeb, na vzdálené síťové entitě.

## Popis

Služba vzdálených operací (ROS) je protokolová služba definovaná v 3GPP pro umožnění interakcí typu vzdáleného volání procedur mezi síťovými entitami, zejména v rámci architektury služeb inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) a IMS. Je specifikována v klíčových protokolových dokumentech, jako jsou 29.078 ([CAMEL](/mobilnisite/slovnik/camel/)) a 29.278 (CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/))). ROS poskytuje standardizovaný způsob, jak jedna entita (vyvolavatel) může požádat o provedení operace na vzdálené entitě (provedovatel) a přijmout odpověď. Strukturuje interakce pomocí operačních kódů, argumentů a výsledků a spravuje korelace mezi požadavky a odpověďmi.

Architektonicky je ROS vrstvou v zásobníku protokolu CAMEL Application Part (CAP), který sám používá Transaction Capabilities Application Part ([TCAP](/mobilnisite/slovnik/tcap/)) a Signalizační systém č. 7 ([SS7](/mobilnisite/slovnik/ss7/)) jako transport. V kontextu IMS mohou platit podobné principy přes protokoly založené na IP. Mezi klíčové komponenty patří poskytovatel ROS, který nabízí sadu operací, a uživatel ROS, který je vyvolává. Operace jsou definovány v ASN.1 a mohou být různých tříd: Třída 1 (synchronní, s hlášením úspěchu i chyby), Třída 2 (asynchronní, pouze s hlášením úspěchu), Třída 3 (asynchronní, pouze s hlášením chyby) a Třída 4 (asynchronní, bez hlášení).

Jak to funguje: vyvolavatel odešle komponentu ROS Invoke obsahující Invoke-ID, operační kód specifikující požadovanou akci (např. 'Connect' pro zřízení hovoru, 'RequestReportBCSMEvent' pro monitorování událostí hovoru) a přidružené parametry. Provedovatel operaci provede a vrátí komponentu ROS Return Result (při úspěchu) se stejným Invoke-ID a případnými výslednými daty, nebo komponentu ROS Return Error, pokud operace selže. Tento mechanismus zajišťuje spolehlivý, korelovaný dialog mezi body řízení služeb ([SCP](/mobilnisite/slovnik/scp/)) a přepojovacími body ([MSC](/mobilnisite/slovnik/msc/), [GMSC](/mobilnisite/slovnik/gmsc/)).

Jeho role je zásadní pro implementaci služeb CAMEL, jako jsou předplacené služby, kontrola podvodů a funkce virtuální privátní sítě (VPN). Umožňuje, aby servisní logika sídlící v centrálním SCP vzdáleně v reálném čase řídila zpracování hovoru v MSC. Tím, že abstrahuje detaily vzdáleného volání procedur, ROS zjednodušuje vývoj síťově nezávislé servisní logiky a zajišťuje interoperabilitu mezi zařízeními od různých výrobců.

## K čemu slouží

ROS byl vytvořen, aby vyřešil potřebu standardizovaného, robustního mechanismu pro řízení služeb inteligentní sítě v okruhově i paketově přepínaných doménách. Před standardizovanými architekturami IN, jako je CAMEL, byly pokročilé služby těsně integrovány do proprietárního softwaru výrobců ústředen, což činilo vytváření služeb pomalým, nákladným a nepřenositelným. To omezovalo inovace a vytvářelo pro operátory závislost na dodavateli.

Problém, který ROS řeší, je poskytnutí čistého, abstrahovaného rozhraní pro vzdálené provádění servisní logiky. Umožňuje oddělení řízení služeb (v SCP) od přepojování hovorů (v MSC), což je základní princip inteligentních sítí. Toto oddělení umožňuje operátorům rychle zavádět nové služby aktualizací centrálních SCP bez nutnosti modifikovat každou ústřednu v síti. Jeho zavedení ve vydání 8 (pro specifikace 3GPP, ačkoli koncepty IN jsou starší) formalizovalo tyto protokoly v rámci 3GPP pro vývoj GSM a UMTS.

Historicky je ROS založen na prvku služby vzdálených operací (ROSE) od ITU-T ze standardů X.400 a OSI, upraveném pro telekomunikační prostředí. Řešil omezení ad-hoc signalizace pro řízení služeb tím, že poskytl strukturovaný, objektově orientovaný model s definovaným zpracováním chyb a korelací. To motivovalo vytvoření interoperabilních, více-dodavatelských sítí CAMEL, které byly klíčové pro umožnění přeshraničního roamingu s předplacenými službami a dalších pokročilých telefonních služeb v éře 2G/3G, přičemž její principy přetrvávají v řízení služeb IMS.

## Klíčové vlastnosti

- Poskytuje rámec vzdáleného volání procedur (RPC) pro telekomunikační servisní logiku.
- Definuje třídy operací (1-4) pro podporu synchronních a asynchronních interakcí s hlášením nebo bez něj.
- Používá protokolové komponenty Invoke, Return Result a Return Error pro strukturovaný dialog.
- Zajišťuje korelaci mezi požadavkem a odpovědí pomocí jedinečných Invoke-ID.
- Tvoří základní servisní vrstvu protokolu CAMEL Application Part (CAP).
- Umožňuje řízení zpracování hovoru/relace v reálném čase ze vzdáleného bodu řízení služeb (SCP).

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)
- [SCP – Service Communication Proxy](/mobilnisite/slovnik/scp/)
- [TCAP – Transaction Capabilities Application Part](/mobilnisite/slovnik/tcap/)

## Definující specifikace

- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4

---

📖 **Anglický originál a plná specifikace:** [ROS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ros/)
