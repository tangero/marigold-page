---
slug: "sw1-sw2"
url: "/mobilnisite/slovnik/sw1-sw2/"
type: "slovnik"
title: "SW1/SW2 – Status Word 1 / Status Word 2"
date: 2025-01-01
abbr: "SW1/SW2"
fullName: "Status Word 1 / Status Word 2"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sw1-sw2/"
summary: "Dva jednotlivé bajty, které tvoří stavový kód (Status Word, SW). SW1 je první bajt, který často označuje třídu odpovědi (normální, varování, chyba). SW2 je druhý bajt, který poskytuje kvalifikátor neb"
---

SW1/SW2 je dvoubajtový stavový kód (Status Word), kde SW1 je první bajt označující třídu odpovědi a SW2 je druhý bajt poskytující podrobný kvalifikátor v rámci této třídy.

## Popis

SW1 a SW2 jsou součásti dvoubajtové odpovědi stavového kódu (SW) v komunikaci se smart kartou. Vždy se přenášejí a analyzují jako pár. SW1, bajt vyššího řádu, typicky definuje obecnou kategorii nebo třídu odpovědi. Například hodnoty SW1 jako '61', '62', '63', '6A' nebo '90' označují různé třídy, jako je 'normální zpracování s dodatečnými informacemi', 'varování', 'chyba provedení' nebo 'normální ukončení'. SW2, bajt nižšího řádu, poskytuje konkrétní význam nebo kvalifikátor v rámci třídy definované SW1. Například, pokud je SW1 '61' (varování, normální odpověď), hodnota v SW2 udává přesný počet datových bajtů, které jsou stále k dispozici ke čtení v následujícím příkazu GET RESPONSE.

Tato technická operace je nedílnou součástí struktury odpovědi [APDU](/mobilnisite/slovnik/apdu/) (Application Protocol Data Unit). Poté, co terminál odešle příkazové APDU (obsahující CLA, INS, P1, P2 a případně data) na UICC, operační systém nebo aplikace karty jej zpracuje. Po dokončení formuluje odpověď. Tato odpověď se skládá z volitelných vrácených dat (tělo odpovědi) následovaných povinnou dvoubajtovou koncovkou: nejprve SW1 a poté SW2. Software terminálu musí tyto bajty analyzovat sekvenčně. Interpretace se provádí pomocí vyhledávání v standardizovaných tabulkách v [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 7816-4 a 3GPP TS 31.102 (pro příkazy specifické pro [USIM](/mobilnisite/slovnik/usim/)).

Jejich úlohou je umožnit přesné a efektivní zpracování chyb a řízení toku. Oddělením odpovědi na třídu (SW1) a detail (SW2) systém umožňuje jak obecné zpracování (např. 'jakákoli chyba v rozsahu 6Axx je chyba parametru'), tak specifické akce (např. SW='6A86' znamená 'nesprávné P1 P2'). To je klíčové pro robustnost procedur, jako je přístup k souborům, autentizace a správa profilů na UICC. Logika terminálu se může větvit na základě dvojice SW1/SW2 a rozhodovat, zda příkaz opakovat, vyžádat si více dat, nebo operaci ukončit a upozornit uživatele.

## K čemu slouží

SW1 a SW2 existují, aby rozložily stavový kód na strukturovaný, hierarchický kód pro efektivnější a logičtější zpracování terminálem. Jediný, monolitický návratový kód by byl méně intuitivní pro analýzu a kategorizaci. Toto rozdělení umožňuje seskupit rodinu souvisejících chybových nebo varovných stavů pod společnou předponu SW1, což zjednodušuje návrh softwaru. Řeší potřebu jak určení výsledku na vysoké úrovni, tak diagnostických informací na nízké úrovni.

Tato struktura byla převzata ze standardů pro smart karty [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 7816, které byly navrženy pro širokou škálu karetních aplikací mimo telekomunikace. 3GPP tento osvědčený model pro UICC přijalo, aby zajistilo globální interoperabilitu a využilo stávající odborné znalosti v oboru. Účelem je poskytnout kompaktní, ale vysoce výstižný prostředek komunikace z omezeného prostředí smart karty k výkonnějšímu procesoru terminálu. Řeší problém sdělení široké škály možných stavů provedení příkazu – od úspěchu s doplňkovými daty po fatální bezpečnostní selhání – s využitím pouze dvou bajtů režie, což je klíčové pro efektivní nízkouhladinovou komunikaci.

## Klíčové vlastnosti

- SW1 je první bajt označující třídu nebo kategorii odpovědi
- SW2 je druhý bajt poskytující specifický kvalifikátor nebo detailní kód
- Vždy přenášeny a interpretovány jako pár (SW1||SW2)
- Umožňuje hierarchické zpracování chybových a stavových kódů
- Definováno v ISO/IEC 7816-4 s rozšířeními specifickými pro 3GPP v TS 31.102
- Základní pro analýzu odpovědi APDU a řízení logického toku v terminálu

## Související pojmy

- [APDU – Application Protocol Data Unit](/mobilnisite/slovnik/apdu/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification

---

📖 **Anglický originál a plná specifikace:** [SW1/SW2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/sw1-sw2/)
