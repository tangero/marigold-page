---
slug: "snrm"
url: "/mobilnisite/slovnik/snrm/"
type: "slovnik"
title: "SNRM – Set Normal Response Mode"
date: 2025-01-01
abbr: "SNRM"
fullName: "Set Normal Response Mode"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/snrm/"
summary: "SNRM je specifický typ rámce v sadě protokolů High-Level Data Link Control (HDLC), používaný k navázání datového spojení v režimu normální odezvy (Normal Response Mode, NRM). Konfiguruje sekundární st"
---

SNRM je rámec High-Level Data Link Control (HDLC) používaný k navázání datového spojení v režimu normální odezvy (Normal Response Mode), který konfiguruje sekundární stanice pro komunikaci pod řízením primární stanice.

## Popis

Set Normal Response Mode (SNRM) je příkazový rámec definovaný v rámci protokolu High-Level Data Link Control ([HDLC](/mobilnisite/slovnik/hdlc/)), což je bitově orientovaný protokol linkové vrstvy standardizovaný [ISO](/mobilnisite/slovnik/iso/). HDLC zajišťuje spolehlivou, bezchybnou komunikaci přes point-to-point a multipoint spoje. SNRM patří mezi nečíslované (Unnumbered, U) rámce, což znamená, že neobsahuje sekvenční čísla a slouží pro účely správy spoje. Jeho specifickou funkcí je přepnutí sekundární stanice do režimu normální odezvy (Normal Response Mode, [NRM](/mobilnisite/slovnik/nrm/)). V NRM může sekundární stanice vysílat data pouze tehdy, když je k tomu explicitně vyzvána (polled) primární stanicí, která si udržuje plnou kontrolu nad spojením. Rámec SNRM obsahuje parametry, které konfigurují provozní charakteristiky spoje, jako je velikost okna (počet povolených nepotvrzených rámců) a modulus (modulo 8 nebo modulo 128 pro sekvenční čísla).

Z architektonického hlediska HDLC pracuje s primární stanicí, která vydává příkazy, a sekundární stanicí, která odpovídá. Příkaz SNRM je odeslán z primární stanice na konkrétní sekundární stanici (adresovanou v adresním poli rámce) k inicializaci datového spoje. Po přijetí platného SNRM sekundární stanice odpoví rámcem Unnumbered Acknowledgment ([UA](/mobilnisite/slovnik/ua/)), pokud parametry přijme, čímž se spojení v NRM naváže. Pokud jsou parametry nepřijatelné, může odpovědět rámcem Frame Reject ([FRMR](/mobilnisite/slovnik/frmr/)). Jakmile je stanice v NRM, musí před odesláním jakýchkoli informačních (Information, I) rámců čekat na příkaz Receive Ready ([RR](/mobilnisite/slovnik/rr/)) od primární stanice. Tato metoda řízeného přístupu je efektivní pro nevyvážené konfigurace, kde jedna stanice (primární) je centrálním řadičem, což je typické pro starší telekomunikační scénáře, jako je připojení řadiče základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) k více základnovým přenosovým stanicím ([BTS](/mobilnisite/slovnik/bts/)).

Jak to funguje, zahrnuje výměnu těchto dohledových rámců. Primární stanice odešle SNRM k nastavení spoje. Rámec obsahuje řídicí informace specifikující režim a provozní parametry. Řadič HDLC sekundární stanice tento příkaz zpracuje, nakonfiguruje svůj interní stavový automat pro NRM a potvrdí pomocí UA. Po tomto handshake může začít přenos dat pod režimem dotazování (polling) primární stanice. SNRM je klíčový pro stanovení počátečního stavu spoje a zajištění shody obou konců na pravidlech komunikace. Je to základní krok v proceduře navazování spoje HDLC, který předchází jakékoli výměně dat. I když jsou HDLC a jeho režimy, jako je NRM, v moderních all-IP sítích považovány za zastaralé, stále jsou relevantní pro určitá backhaulová rozhraní, starší síťové prvky a jako konceptuální základ pro pochopení protokolů řízení datového spoje.

## K čemu slouží

SNRM existuje, aby poskytl standardizovanou, spolehlivou metodu pro navázání řízeného datového spojení typu master-slave jako součást sady protokolů HDLC. Řeší problém inicializace komunikace na datovém spoji, kde jedna stanice (primární) musí koordinovat a řídit přenosovou aktivitu jedné nebo více sekundárních stanic. Před protokoly jako HDLC bylo řízení datového spoje často ad-hoc, což vedlo ke kolizím, neefektivitě a nespolehlivému přenosu dat v multipoint konfiguracích. Vytvoření SNRM a NRM bylo motivováno potřebou strukturovaného přístupu ke správě spojů v telekomunikačních sítích, zejména pro rozhraní jako rozhraní Abis mezi BSC a BTS v sítích GSM.

Historicky, s rozvojem digitálních telekomunikací, vznikla potřeba robustního protokolu datového spoje pro řídicí a managementovou rovinu. HDLC, vyvinutý ISO, se široce rozšířil. Režim normální odezvy (NRM), iniciovaný SNRM, byl navržen pro prostředí s jasným centrálním řadičem a více vzdálenými terminály – běžná topologie v raných digitálních sítích. Odstranil omezení jednodušších protokolů tím, že poskytl explicitní nastavení spoje, vyjednávání parametrů a řízený přístup, což zabránilo nežádaným přenosům ze sekundárních stanic, které by mohly způsobit kolize dat na sdílených linkách.

Motivací bylo zajistit uspořádanou, na chybách kontrolovanou komunikaci pro kritické síťové signalizace a provozní a údržbový provoz. SNRM umožňuje primární stanici efektivně spravovat zdroje spoje a dotazovat sekundární stanice pouze tehdy, když mají data k odeslání nebo když je potřeba zjistit jejich stav. Tím se šetří šířka pásma a zjednodušuje se návrh sekundárních stanic. Zatímco Asynchronous Response Mode (ARM) a Balanced Mode (ABM) byly později definovány pro více peer-to-peer scénáře, NRM iniciovaný SNRM zůstal základním kamenem mnoha starších telekomunikačních rozhraní a poskytoval spolehlivost vyžadovanou pro síťové řídicí funkce.

## Klíčové vlastnosti

- Nečíslovaný (Unnumbered, U) rámec HDLC používaný pro navázání spoje
- Přepne sekundární stanici do režimu normální odezvy (Normal Response Mode, NRM)
- Obsahuje vyjednatelné parametry, jako je velikost okna a modulus
- Vyžaduje potvrzení pomocí rámce UA pro úspěšné nastavení
- Umožňuje primární stanicí řízený, dotazovací (polled) přístup pro sekundární stanice
- Základní pro nevyvážené, multipoint konfigurace spojů

## Definující specifikace

- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP

---

📖 **Anglický originál a plná specifikace:** [SNRM na 3GPP Explorer](https://3gpp-explorer.com/glossary/snrm/)
