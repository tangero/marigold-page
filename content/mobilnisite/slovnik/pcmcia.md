---
slug: "pcmcia"
url: "/mobilnisite/slovnik/pcmcia/"
type: "slovnik"
title: "PCMCIA – Personal Computer Memory Card International Association"
date: 2026-01-01
abbr: "PCMCIA"
fullName: "Personal Computer Memory Card International Association"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pcmcia/"
summary: "Standardní rozhraní pro přidávání rozšiřujících karet do počítačů, historicky používané pro rané karty pro mobilní data (např. GSM/GPRS PC Cards). Umožňovalo přenosné připojení díky standardizovanému"
---

PCMCIA je standardní rozhraní pro přidávání rozšiřujících karet (jako například rané GSM/GPRS modemy pro mobilní data) do počítačů, umožňující přenosné připojení a přístup k mobilnímu širokopásmovému internetu.

## Popis

Standard Personal Computer Memory Card International Association (PCMCIA) definuje fyzický formát a elektrické rozhraní pro rozšiřující karty, běžně známé jako [PC](/mobilnisite/slovnik/pc/) Cards. V kontextu 3GPP byly PCMCIA karty používány jako externí modemy nebo síťové karty ([NIC](/mobilnisite/slovnik/nic/)) k zajištění mobilního připojení pro notebooky a jiná přenosná zařízení. Tyto karty obsahovaly potřebný rádiový transceiver, základnový procesor a slot pro [SIM](/mobilnisite/slovnik/sim/) kartu, což umožňovalo hostitelskému zařízení připojit se ke sítím GSM, [GPRS](/mobilnisite/slovnik/gprs/) nebo později UMTS. Samotné rozhraní je 68pinový konektor podporující 16bitový nebo 32bitový (CardBus) přenos dat, se specifikacemi pro správu napájení a možností zaživa vyměnitelných zařízení (hot-swapping).

Z architektonického hlediska funguje karta pro mobilní data založená na PCMCIA jako samostatný terminál. Zahrnuje funkce mobilního zařízení ([ME](/mobilnisite/slovnik/me/)) včetně rádiové jednotky a protokolových zásobníků pro rozhraní vzduchem (např. Um, Uu) a s hostitelským zařízením komunikuje přes PCMCIA sběrnici. Hostitel spouští funkci adaptace terminálu ([TAF](/mobilnisite/slovnik/taf/)) nebo ovladače zařízení, které kartu prezentují operačnímu systému jako síťový adaptér. Komunikace mezi hostitelem a kartou využívá standardizované AT příkazy ([ETSI](/mobilnisite/slovnik/etsi/)/3GPP TS 27.007) přes virtuální sériový port, který ovladač vytváří. Karta zpracovává všechny protokoly vrstvy 1 (fyzické) a vrstvy 2 (spojové), zatímco protokoly vyšších vrstev, jako je IP, typicky zpracovává hostitelský [TCP/IP](/mobilnisite/slovnik/tcp-ip/) zásobník.

Klíčové komponenty PCMCIA karty pro mobilní data zahrnují RF front-end pro konkrétní pásmo mobilní sítě (např. 900 MHz, 1800 MHz), základnový procesor provádějící firmware modemu, paměť pro ukládání a řídicí čip PCMCIA rozhraní spravující komunikaci s hostitelem. Karta také obsahuje slot pro modul identifikace účastníka (SIM), který je nezbytný pro autentizaci v síti a identifikaci účastníka. Role PCMCIA v sítích 3GPP byla primárně jako faktor uživatelského zařízení (UE), umožňující datové služby před rozšířením integrovaných modemů a USB konektorů. Byla klíčovým mostem pro přijetí mobilních dat na počátku roku 2000.

Z pohledu sítě se zařízení používající PCMCIA kartu jeví jako standardní mobilní stanice pro jádro sítě. Provádí běžné procedury jako přihlášení (attach), autentizaci a aktivaci PDP kontextu. Síť s ním zachází shodně jako s mobilním telefonem, směruje data přes uzel podpory služeb GPRS (SGSN) a bránový uzel podpory služeb GPRS (GGSN). Role PCMCIA rozhraní je pro síť transparentní; jde čistě o lokální rozhraní mezi hostitelem a modemem. Jeho význam spočívá ve standardizaci fyzického a logického připojení, což zajišťuje interoperabilitu mezi kartami různých výrobců a hostitelskými zařízeními, což urychlilo vývoj trhu s příslušenstvím pro mobilní data.

## K čemu slouží

Standard PCMCIA byl vytvořen pro řešení potřeby univerzálního kompaktního formátu rozšiřující karty pro přenosné počítače. Před jeho přijetím bylo přidávání paměti, úložiště nebo síťových funkcí do notebooků neohrabané a závislé na konkrétním výrobci. Standard PCMCIA, zavedený na počátku 90. let 20. století, poskytl společný formát a rozhraní, což umožnilo vznik trhu zaměnitelných příslušenství. To bylo klíčové pro mobilitu výpočetní techniky, protože uživatelé mohli rozšiřovat možnosti svých notebooků bez vnitřních úprav.

V telekomunikační oblasti řešilo PCMCIA problém připojení přenosných počítačů k mobilním sítím. Před příchodem integrovaných mobilních modemů a všudypřítomného USB byl slot PCMCIA primárním rozšiřujícím portem na noteboocích. Mobilní operátoři a výrobci zařízení využili tento standard k vytvoření karet pro mobilní data, což umožnilo přístup k mobilnímu internetu pro firemní uživatele a první uživatele nových technologií. Řešilo to omezení pevné linky vytáčeného připojení nebo kabelového Ethernetu tím, že poskytovalo skutečnou mobilitu, což uživatelům umožňovalo připojení odkudkoli s pokrytím mobilní sítě.

Historický kontext představuje vzestup datových služeb GSM (přepojování okruhů a později GPRS) na konci 90. let a počátku roku 2000. Formát PCMCIA byl dominantním řešením pro poskytování těchto služeb rostoucímu trhu s notebooky. Tvořil most mezi světem mobilních komunikací (s jeho specializovanými modemy a SIM kartami) a světem PC (s jeho standardní rozšiřující sběrnicí). I když byl později nahrazen standardy ExpressCard, USB modemy a vestavěnými moduly, PCMCIA byl zásadní pro popularizaci mobilního širokopásmového připojení.

## Klíčové vlastnosti

- Standardizované 68pinové rozhraní pro interoperabilitu
- Možnost výměny za provozu (hot-swapping), umožňující vložení/vyjmutí karty bez vypnutí hostitele
- Podpora 16bitové a 32bitové (CardBus) šířky datové sběrnice
- Integrovaná správa napájení pro provoz s nízkou spotřebou v mobilních zařízeních
- Fyzický formát (Typ I, II, III) pro různé tloušťky karet
- Společné programové rozhraní využívající sadu AT příkazů přes virtuální sériový port

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework

---

📖 **Anglický originál a plná specifikace:** [PCMCIA na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcmcia/)
