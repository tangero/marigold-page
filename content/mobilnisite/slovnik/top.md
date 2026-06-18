---
slug: "top"
url: "/mobilnisite/slovnik/top/"
type: "slovnik"
title: "TOP – Tuak Operator Variant Algorithm Configuration Field"
date: 2025-01-01
abbr: "TOP"
fullName: "Tuak Operator Variant Algorithm Configuration Field"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/top/"
summary: "TOP je konfigurační pole používané v autentizačním a dohodovacím algoritmu klíčů TUAK. Umožňuje operátorům mobilních sítí přizpůsobit a odlišit jejich implementaci kryptografických funkcí TUAK, čímž p"
---

TOP je konfigurační pole v autentizačním algoritmu TUAK, které umožňuje mobilním operátorům přizpůsobit jeho kryptografické funkce a vytvořit tak bezpečnostní varianty specifické pro operátora.

## Popis

Konfigurační pole varianty algoritmu pro operátora TUAK (TOP) je parametr definovaný v bezpečnostních specifikacích 3GPP pro sadu autentizačních algoritmů TUAK. TUAK (což označuje sadu algoritmů založených na permutaci Keccak) je standardizovaná sada kryptografických funkcí vyvinutá skupinou [ETSI](/mobilnisite/slovnik/etsi/) [SAGE](/mobilnisite/slovnik/sage/) jako alternativa ke staršímu algoritmu MILENAGE, který je založen na [AES](/mobilnisite/slovnik/aes/). TOP je klíčová komponenta poskytující přizpůsobení. Je v podstatě vstupní hodnotou konfigurace, která spolu s dalšími vstupy, jako je tajný klíč účastníka (K), ovlivňuje výstup funkcí algoritmu TUAK (f1, f1*, f2, f3, f4, f5, f5*).

Z architektonického hlediska je TOP uložen v Autentizačním centru (AuC) v síti operátora a je asociován s profilem účastníka. Během autentizační procedury, když AuC generuje autentizační vektor (obsahující [RAND](/mobilnisite/slovnik/rand/), [AUTN](/mobilnisite/slovnik/autn/), [XRES](/mobilnisite/slovnik/xres/), [CK](/mobilnisite/slovnik/ck/), [IK](/mobilnisite/slovnik/ik/)), používá jako vstupy do algoritmů TUAK klíč účastníka (K) a hodnotu TOP specifickou pro operátora. Výsledný autentizační vektor je odeslán do obslužné sítě (VLR/SGSN/MME). Mobilní stanice (USIM) také disponuje stejnou hodnotou K a TOP. Když obdrží od sítě RAND a AUTN, provede stejné výpočty TUAK pomocí svého uloženého K a TOP. Pokud se hodnoty TOP shodují, může USIM úspěšně ověřit AUTN a vypočítat odpovídající RES, CK a IK.

Úlohou TOP je zavést do kryptografických výpočtů variabilitu specifickou pro operátora, aniž by se měnil základní algoritmus Keccak. To znamená, že i když je specifikace základního algoritmu TUAK veřejná, efektivní algoritmus používaný operátorem je jedinečný díky tajné hodnotě TOP. TOP funguje jako dodatečný tajný parametr vedle klíče K, čímž zvyšuje složitost pro útočníka, který by mohl získat kompromitovanou univerzální implementaci TUAK. TOP je typicky 128bitová nebo 256bitová hodnota, což odpovídá bezpečnostní síle algoritmu. Jeho správa je odpovědností operátora a přidává vrstvu síťově specifického bezpečnostního přizpůsobení nad rámec standardizovaného autentizačního rámce.

## K čemu slouží

TOP byl vytvořen, aby řešil potřebu kryptografických algoritmů odlišených pro operátora v rámci globálního standardu. Před TUAK byl hlavním algoritmem 3GPP MILENAGE, který, ač standardizovaný, neměl vestavěné pole pro přizpůsobení operátorem. Pokud by byl algoritmus MILENAGE kdy kompromitován nebo byla nalezena jeho slabina, všechny sítě jej používající by byly současně zranitelné. Zavedení TUAK, a konkrétně pole TOP, bylo motivováno snahou o kryptografickou agilitu a varianty specifické pro operátora.

Tento přístup řeší několik problémů. Za prvé zmírňuje riziko, že jediná kryptografická chyba ovlivní celý ekosystém; chyba zneužívající základní funkci Keccak by stále vyžadovala znalost konkrétního TOP operátora, aby byla účinná proti síti tohoto operátora. Za druhé umožňuje operátorům nasadit jejich vlastní 'verzi' autentizačního algoritmu, což může být přínosné pro splnění specifických národních regulatorních požadavků nebo pro implementaci proprietárních bezpečnostních vylepšení. TOP v podstatě přesouvá část 'tajemství' algoritmu z pouhého klíče účastníka (K) na kombinaci K a síťově specifické konfigurace, čímž vytváří dvouúrovňovou tajnou strukturu. To byla součást širšího úsilí 3GPP ve vydáních jako 12 a novějších o zvýšení robustnosti zabezpečení a poskytnutí více nástrojů operátorům pro nezávislé řízení jejich bezpečnostního postavení.

## Klíčové vlastnosti

- Konfigurační parametr specifický pro operátora pro sadu algoritmů TUAK
- Vstup do kryptografických funkcí TUAK (f1-f5*) spolu s klíčem účastníka K
- Uložen v AuC a v USIM
- Umožňuje vytváření variant autentizačního algoritmu jedinečných pro operátora
- Zvyšuje bezpečnost přidáním druhého tajného faktoru do výpočtu algoritmu
- Podporuje možnosti kryptografické síly 128 bitů a 256 bitů

## Související pojmy

- [AUC – Authentication Centre](/mobilnisite/slovnik/auc/)

## Definující specifikace

- **TR 33.834** (Rel-16) — Long Term Key Update Procedures Study
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [TOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/top/)
