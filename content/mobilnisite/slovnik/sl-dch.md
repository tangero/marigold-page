---
slug: "sl-dch"
url: "/mobilnisite/slovnik/sl-dch/"
type: "slovnik"
title: "SL-DCH – Sidelink Discovery Channel"
date: 2025-01-01
abbr: "SL-DCH"
fullName: "Sidelink Discovery Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sl-dch/"
summary: "Fyzický kanál v LTE sidelinku používaný pro objevování zařízení ve službách blízkosti (ProSe). Umožňuje UE objevovat blízká zařízení vysíláním a monitorováním objevovacích zpráv a tvoří základ pro nav"
---

SL-DCH je fyzický kanál v LTE sidelinku používaný pro objevování zařízení v rámci služeb blízkosti (Proximity Services), který umožňuje UE vysílat a monitorovat zprávy za účelem nalezení blízkých zařízení pro komunikaci typu D2D.

## Popis

Sidelink Discovery Channel (SL-DCH) je fyzický kanál definovaný pro komunikace založené na LTE sidelinku, který usnadňuje objevování zařízení v rámci architektury služeb blízkosti ([ProSe](/mobilnisite/slovnik/prose/)) 3GPP. Tento kanál umožňuje uživatelským zařízením (UE) objevovat a být objevována jinými blízkými zařízeními prostřednictvím vysílání a příjmu objevovacích zpráv obsahujících identifikátory aplikační vrstvy nebo jiné objevovací informace. V mnoha scénářích fungující nezávisle na infrastruktuře mobilní sítě poskytuje SL-DCH základní mechanismus, který umožňuje zařízením identifikovat potenciální komunikační partnery před navázáním přímých [D2D](/mobilnisite/slovnik/d2d/) spojení pro výměnu dat nebo skupinovou komunikaci.

Z architektonického hlediska existuje SL-DCH ve fyzické vrstvě protokolového zásobníku LTE sidelinku, přičemž podrobné specifikace jsou uvedeny v dokumentech 3GPP TS 36.212 pro zpracování fyzické vrstvy a 36.300 pro celkovou systémovou architekturu. Kanál využívá vyhrazené objevovací zdroje ve speciálně konfigurovaných fondech objevovacích zdrojů, které mohou být přiděleny sítí při pokrytí nebo předkonfigurovány pro provoz mimo pokrytí. Přenosy na SL-DCH se skládají z transportních bloků pro objevování, které nesou objevovací zprávy, přičemž každá zpráva obsahuje informace jako ProSe Application Codes, ProSe Application Identifiers nebo jiná data související s objevováním. Kanál používá modulaci [QPSK](/mobilnisite/slovnik/qpsk/) s turbokódováním pro opravu chyb, optimalizovanou pro vysílací charakter objevovacích přenosů, kde může monitorovat více neznámých přijímačů.

V provozu podporuje SL-DCH dva základní objevovací modely: Model A (oznámení typu „jsem tady“) a Model B (dotazy typu „kdo je tam?“ a odpovědi). V Modelu A UE periodicky vysílá objevovací zprávy na SL-DCH, aby oznámila svou přítomnost a dostupnost pro komunikaci. Jiná UE monitorují fond objevovacích zdrojů a přijímají tato oznámení bez vysílání jakékoli odpovědi na samotném objevovacím kanálu. V Modelu B jedno UE vysílá objevovací zprávu obsahující dotaz a cílená UE odpovídají objevovacími zprávami s příslušnými odpověďmi. Oba modely využívají stejnou strukturu fyzického kanálu SL-DCH, ale liší se v procedurách vyšších vrstev řídících obsah zpráv a časování.

Technická implementace zahrnuje specifické zpracování na fyzické vrstvě včetně kódování kanálu, skramblování, modulace, mapování vrstev, předkódování a mapování na zdrojové prvky podle specifikací LTE sidelinku. Objevovací zdroje jsou organizovány do objevovacích period, přičemž každá perioda obsahuje více objevovacích podrámců, ve kterých může docházet k přenosům SL-DCH. UE vybírají konkrétní objevovací zdroje ve fondu pomocí síťově přidělených vzorů nebo autonomních výběrových algoritmů, které pomáhají minimalizovat kolize mezi současnými objevovacími přenosy. Návrh kanálu zahrnuje mechanismy pro zvládání poloduplexních omezení (kdy UE nemůže současně vysílat a přijímat) a pro správu interference mezi objevovacími přenosy a jinými sidelink nebo mobilními komunikacemi.

SL-DCH hraje klíčovou roli při umožňování služeb založených na blízkosti tím, že poskytuje počáteční kontaktní mechanismus mezi zařízeními. V aplikacích pro veřejnou bezpečnost umožňuje záchranářům zjistit vzájemnou přítomnost i mimo síťové pokrytí, což umožňuje následné vytvoření přímých komunikačních skupin. Pro komerční aplikace ProSe umožňuje funkce sociálních sítí, kde uživatelé mohou objevovat přátele nebo služby ve svém bezprostředním okolí. Návrh kanálu vyvažuje spolehlivost objevování s energetickou účinností, protože zařízení mohou potřebovat monitorovat po delší dobu při provozu na baterii. Standardizací fyzické vrstvy pro objevování zajistilo 3GPP interoperabilitu mezi zařízeními od různých výrobců a vytvořilo základ pro inovativní aplikace založené na blízkosti.

## K čemu slouží

SL-DCH byl vytvořen, aby řešil základní požadavek na objevování zařízení v architektuře služeb blízkosti ([ProSe](/mobilnisite/slovnik/prose/)) 3GPP zavedené ve vydání 12. Před jeho standardizací bylo objevování zařízení typu zařízení-zařízení závislé na nemobilních technologiích, jako je Bluetooth nebo Wi-Fi Direct, kterým chyběla integrace s mobilními sítěmi, fungovaly v neregulovaném spektru s možnými problémy s interferencí a nemohly využít asistenci mobilní sítě pro rozšířenou funkčnost. Tato omezení byla zvláště problematická pro aplikace veřejné bezpečnosti, kde bylo spolehlivé zjištění blízkých záchranářů klíčové během mimořádných událostí, kdy mohla být mobilní infrastruktura narušena.

Primární motivace pro SL-DCH vzešla ze dvou odlišných aplikačních domén: komunikací pro veřejnou bezpečnost a komerčních služeb blízkosti. Pro veřejnou bezpečnost bylo spolehlivé objevování zařízení nezbytné pro vytváření přímých komunikačních skupin mezi záchranáři působícími v katastrofických oblastech s poškozenou síťovou infrastrukturou. Pro komerční aplikace chtěli mobilní operátoři umožnit inovativní služby, jako jsou sociální sítě, místní reklama a hry, které využívají fyzickou blízkost uživatelů při zachování integrace s jejich mobilními předplatnými a službami.

SL-DCH tyto problémy vyřešil tím, že poskytl standardizovaný, s mobilní sítí integrovaný objevovací mechanismus fungující v regulovaném spektru s předvídatelnými výkonnostními charakteristikami. Vyřešil omezení předchozích přístupů tím, že nabídl objevování asistované sítí, když byla infrastruktura dostupná (což zlepšuje účinnost a řízení), a zároveň podporoval autonomní objevování při provozu mimo pokrytí (zajišťuje funkčnost ve všech scénářích). Návrh kanálu konkrétně zohledňoval jedinečné požadavky objevovacích operací, včetně podpory anonymního objevování (kdy zařízení objevují služby bez odhalení identity uživatele), energeticky účinných monitorovacích vzorů a škálovatelného provozu od řídkého až po husté nasazení zařízení. Vytvořením této základní objevovací schopnosti umožnilo 3GPP širší ekosystém aplikací založených na blízkosti, které mohou využívat jak spolehlivost regulovaného spektra, tak integraci se službami mobilní sítě.

## Klíčové vlastnosti

- Fyzický kanál pro objevování zařízení v LTE službách blízkosti (ProSe)
- Podporuje objevování podle Modelu A (na bázi oznámení) i Modelu B (dotaz-odpověď)
- Využívá vyhrazené fondy objevovacích zdrojů konfigurovatelné sítí nebo předkonfigurované
- Funguje ve scénářích s pokrytím i mimo pokrytí sítě
- Používá modulaci QPSK s turbokódováním pro spolehlivý příjem vysílání
- Umožňuje anonymní i neanonymní režimy objevování pro různé aplikační požadavky

## Související pojmy

- [SL-BCH – Sidelink Broadcast Channel](/mobilnisite/slovnik/sl-bch/)

## Definující specifikace

- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [SL-DCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-dch/)
