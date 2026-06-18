---
slug: "sacch-t"
url: "/mobilnisite/slovnik/sacch-t/"
type: "slovnik"
title: "SACCH/T – Slow Associated Control CHannel/Traffic channel"
date: 2025-01-01
abbr: "SACCH/T"
fullName: "Slow Associated Control CHannel/Traffic channel"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sacch-t/"
summary: "Řídicí kanál GSM přidružený k provoznímu kanálu (TCH) pro přenos nezbytné signalizace a měřicích dat nízkou rychlostí. Umožňuje klíčové funkce jako řízení výkonu, časový předstih a hlášení měření běhe"
---

SACCH/T je řídicí kanál GSM přidružený k provoznímu kanálu pro přenos nezbytné signalizace a měřicích dat nízkou rychlostí během aktivního hovoru, který umožňuje funkce jako řízení výkonu a časový předstih.

## Popis

Slow Associated Control CHannel/Traffic channel ([SACCH](/mobilnisite/slovnik/sacch/)/T) je základní signalizační kanál v GSM a jeho vyvinutých sítích 2G/3G, který je specificky spárován s provozním kanálem ([TCH](/mobilnisite/slovnik/tch/)) během aktivního hovoru v okruhově spínané síti. Funguje způsobem časového multiplexu, sdílí stejný fyzický rádiový zdroj (časový slot) jako přidružený TCH, ale využívá specifické rámce v rámci struktury multirámce. SACCH/T přenáší řídicí informace relativně nízkou, pevnou rychlostí, prokládané s uživatelským provozem, což umožňuje síti udržovat a optimalizovat rádiový spoj bez přerušení primárního hlasového nebo datového toku. Jeho hlavní úlohou je přenášet nepřetržité, periodické signalizace nezbytné pro údržbu aktivního spojení.

Z architektonického hlediska je SACCH/T definován v rámci specifikací vrstvy 1 a vrstvy 2 GSM rozhraní. Je namapován na vyhrazený logický kanál, který je vždy přítomen při přidělení TCH. Struktura kanálu využívá pro provozní kanály 26-rámcový multirámec, kde jsou specifické rámce (např. rámec 12 a 25 v multirámci plné rychlosti TCH) určeny pro SACCH/T. Toto řešení zajišťuje periodický přenos řídicí signalizace přibližně každých 480 ms, čímž poskytuje stabilní tok dat pro údržbu spoje. Informace jsou zpracovávány základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)) a mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)), přičemž signalizační zprávy vyšších vrstev jsou předávány řadiči základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)).

Klíčové součásti funkčnosti SACCH/T zahrnují přenos hlášení měření (Measurement Reports) z MS do sítě, která obsahují data o přijímané síle signálu ([RXLEV](/mobilnisite/slovnik/rxlev/)), kvalitě signálu ([RXQUAL](/mobilnisite/slovnik/rxqual/)) a měření sousedních buněk. Naopak síť využívá SACCH/T k odesílání příkazů MS, jako jsou příkazy pro řízení výkonu (Power Control) k úpravě vysílacího výkonu MS a příkazy pro časový předstih (Timing Advance) k synchronizaci časování vysílání, což kompenzuje zpoždění šíření. Dále přenáší zprávy systémových informací (System Information) pro obsluhovanou buňku. Provoz SACCH/T je klíčový pro funkce jako příprava předání hovoru (handover), dohled nad rádiovým spojem a adaptivní řízení vícečetného kodeku, což z něj činí nepostradatelný prvek pro spolehlivou okruhově spínanou komunikaci v sítích GSM, [GPRS](/mobilnisite/slovnik/gprs/) a EDGE.

## K čemu slouží

SACCH/T byl vytvořen k řešení základní potřeby nepřetržité signalizace během hovoru v sítích GSM. V čistě provozním kanálovém spojení nebyl žádný inherentní mechanismus pro výměnu řídicích informací nezbytných pro údržbu spoje, jako je úprava úrovní výkonu nebo sledování kvality signálu, bez přerušení uživatelského hlasového hovoru. Před jeho standardizací by takové řízení vyžadovalo odebrání bitů z hlasového toku nebo vytvoření samostatných signalizačních kanálů, což by bylo neefektivní nebo rušivé. SACCH/T poskytuje vyhrazený kanál s nízkou šířkou pásma multiplexovaný s provozem, což tento problém elegantně řeší.

Jeho zavedení ve vydání 5 (ačkoli koncepčně byl součástí původního návrhu GSM) formalizovalo jeho roli v rámci specifikačního rámce 3GPP pro systémy 2G. Hlavní problémy, které řeší, jsou udržování kvality rádiového spoje a umožnění mobility řízené sítí. Poskytnutím nepřetržitého kanálu pro hlášení měření může síť činit informovaná rozhodnutí o předání hovoru. Přenosem příkazů pro řízení výkonu a časový předstih optimalizuje využití rádiových zdrojů, snižuje interference a prodlužuje výdrž baterie. Tento trvalý signalizační kanál umožňuje stabilní, dlouhotrvající okruhově spínané hovory v celulárních sítích a tvoří základní princip, který byl později v různých formách adaptován pro řídicí kanály 3G a 4G.

## Klíčové vlastnosti

- Je přidružen k vyhrazenému provoznímu kanálu (TCH) během aktivních hovorů
- Přenáší periodická hlášení měření (RXLEV, RXQUAL, informace o sousedních buňkách)
- Přenáší síťové příkazy pro řízení výkonu (Power Control) a časový předstih (Timing Advance)
- Využívá specifické rámce v rámci 26-rámcové struktury multirámce TCH
- Umožňuje dohled nad rádiovým spojem a přípravu předání hovoru
- Podporuje přenos systémových informací pro obsluhovanou buňku

## Související pojmy

- [TCH – Traffic Channel](/mobilnisite/slovnik/tch/)
- [FACCH – Fast Associated Control CHannel](/mobilnisite/slovnik/facch/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [SACCH/T na 3GPP Explorer](https://3gpp-explorer.com/glossary/sacch-t/)
