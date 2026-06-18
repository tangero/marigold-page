---
slug: "pcca"
url: "/mobilnisite/slovnik/pcca/"
type: "slovnik"
title: "PCCA – Portable Computer and Communications Association"
date: 2025-01-01
abbr: "PCCA"
fullName: "Portable Computer and Communications Association"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/pcca/"
summary: "PCCA je standardizovaná sada AT příkazů definovaná 3GPP pro řízení datových komunikačních funkcí na mobilních zařízeních. Umožňuje externím aplikacím nebo počítačům spravovat datová připojení, napříkl"
---

PCCA je standardizovaná sada AT příkazů 3GPP pro řízení datové komunikace mobilních zařízení, která umožňuje externím aplikacím spravovat připojení, jako jsou PDP kontexty pro sdílení připojení (tethering) a modemy.

## Popis

Portable Computer and Communications Association (PCCA) označuje sadu AT příkazů standardizovaných v rámci technické specifikace 3GPP 27.007. Tyto příkazy poskytují standardizovaný jazyk pro koncové zařízení (Terminal Equipment, [TE](/mobilnisite/slovnik/te/)), například notebook nebo router, k ovládání jednotky mobilního ukončení (Mobile Termination, [MT](/mobilnisite/slovnik/mt/)), což je modem nebo mobilní zařízení. Sada příkazů PCCA konkrétně řídí služby datové komunikace, umožňující TE zahájit, nakonfigurovat, monitorovat a ukončit datové relace přes mobilní síť. Abstrahuje složitosti podkladové sítě a nabízí konzistentní rozhraní pro aplikace bez ohledu na konkrétní buněčnou technologii (např. GSM, UMTS, LTE).

Z architektonického hlediska PCCA funguje přes fyzické rozhraní, jako je [USB](/mobilnisite/slovnik/usb/), sériové nebo Bluetooth, pomocí modelu příkaz-odpověď. TE odešle řetězec AT příkazu, který MT zpracuje, provede odpovídající akci a vrátí výsledný kód. Klíčové kategorie příkazů v rámci PCCA zahrnují příkazy pro obecné ovládání (AT+CGMI, AT+CGMM), stav registrace v síti (AT+CREG) a nejdůležitěji operace v paketové doméně. Pro datové relace se používají příkazy jako AT+CGDCONT k definování kontextů paketového datového protokolu ([PDP](/mobilnisite/slovnik/pdp/)) se specifikací parametrů, jako je Access Point Name ([APN](/mobilnisite/slovnik/apn/)), zatímco [ATD](/mobilnisite/slovnik/atd/)*99# slouží k zahájení datového volání. MT zajišťuje interakci s jádrem sítě (Core Network), konkrétně se Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) nebo Mobility Management Entity (MME), k založení přenosového kanálu (bearer).

Její role v síti je jako klíčový prostředek rozhraní člověk-stroj (MMI) pro datovou konektivitu. Nachází se na průsečíku uživatelského zařízení a síťových služeb, převádějíc požadavky aplikací vysoké úrovně na síťově specifickou signalizaci. To umožňuje vytváření vestavěných modulů, USB modemů (donglů) a vozidel s integrovanou konektivitou, kterou lze spravovat externími systémy. Standardizace zajišťuje interoperabilitu mezi zařízeními od různých výrobců a podporuje robustní ekosystém pro mobilní datové aplikace nad rámec pouhého použití mobilního telefonu.

## K čemu slouží

PCCA byla vytvořena, aby řešila rostoucí potřebu standardizovaného ovládání datových služeb na mobilních zařízeních externím výpočetním zařízením. Před její standardizací výrobci často používali proprietární sady AT příkazů, což vedlo k fragmentaci a problémům s kompatibilitou. To ztěžovalo vývojářům tvorbu univerzálního softwaru pro sdílení připojení (tethering), telemetrii nebo mobilní širokopásmové aplikace, který by fungoval napříč různými modemy a zařízeními. Standard PCCA, navazující na dědictví ITU-T V.25ter a GSM 07.07, poskytl jednotný příkazový jazyk specificky přizpůsobený pro paketově orientovanou doménu sítí 2.5G, 3G a pozdějších.

Primární problém, který řeší, je abstrakce složitých procedur mobilní sítě pro správu datových relací. Bez PCCA by vývojář aplikace potřeboval hluboké znalosti signalizačních protokolů sítě k navázání datového připojení. Příkazy PCCA tuto složitost skrývají, což vývojářům umožňuje soustředit se na aplikační logiku. To bylo zvláště motivováno nástupem služby General Packet Radio Service (GPRS) a vizí 'vždy připojeného' internetu pro přenosné počítače. Umožnilo komerční úspěch PC datových karet a USB modemů, které byly klíčové pro rané přijetí mobilního širokopásmového připojení.

Dále PCCA podporuje automatizaci a dálkovou správu. Systémy v strojích (automatech, bankomatech) nebo vozidlech mohou používat skripty odesílající PCCA příkazy k navázání konektivity pro přenos dat bez zásahu uživatele. Stala se tak základní technologií pro prostředí komunikace stroj-stroj (M2M), které předcházelo modernímu IoT, a poskytla spolehlivou a standardizovanou metodu pro vestavěné systémy k přístupu do buněčných sítí.

## Klíčové vlastnosti

- Standardizovaná sada AT příkazů pro řízení služeb paketových dat
- Umožňuje definici a aktivaci kontextů paketového datového protokolu (PDP)
- Poskytuje příkazy pro dotazování na identitu a schopnosti modemu
- Podporuje hlášení stavu registrace v síti a kvality signálu
- Umožňuje zahájení a ukončení datového volání (např. ATD*99#)
- Zajišťuje interoperabilitu mezi koncovým zařízením (Terminal Equipment) a mobilními ukončeními (Mobile Termination) od různých výrobců

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 27.007** (Rel-19) — AT Command Set for UE

---

📖 **Anglický originál a plná specifikace:** [PCCA na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcca/)
