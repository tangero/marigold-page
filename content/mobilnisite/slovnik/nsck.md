---
slug: "nsck"
url: "/mobilnisite/slovnik/nsck/"
type: "slovnik"
title: "NSCK – Network Subset Control Key"
date: 2025-01-01
abbr: "NSCK"
fullName: "Network Subset Control Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nsck/"
summary: "Kryptografický klíč používaný v autentizačních algoritmech založených na GSM (varianty COMP128). Je odvozen z hlavního klíče účastníka (Ki) a identifikátoru specifického pro podsíť sítě, což umožňuje"
---

NSCK je kryptografický klíč odvozený z hlavního klíče účastníka a identifikátoru podsítě sítě, který umožňuje diferencované ověřování a šifrování pro sítě GSM a roamingové partnery.

## Popis

Network Subset Control Key (NSCK) je koncept kryptografického klíče z období GSM, definovaný v raných specifikacích 3GPP. Není to samostatný klíč uložený na [SIM](/mobilnisite/slovnik/sim/) kartě, nýbrž odvozený klíč. Proces odvození zahrnuje trvalý tajný klíč účastníka (Ki), který je uložen na SIM kartě a v Autentizačním centru (AuC) operátora, a Identifikátor podsítě sítě ([NSCI](/mobilnisite/slovnik/nsci/)). Pro odvození se používá standardizovaná funkce pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)), například ta definovaná pro algoritmy COMP128. Vzorec je v podstatě NSCK = KDF(Ki, NSCI). Tento proces vytváří klíč specifický pro konkrétní 'podsíť sítě'. Podsíť sítě může být definována jako část [PLMN](/mobilnisite/slovnik/plmn/) (např. pro různé nabídky služeb) nebo, častěji v pozdějším použití, jako síť konkrétního roamingového partnera.

Hlavní funkcí NSCK je sloužit jako vstupní klíč pro GSM autentizační a šifrovací algoritmus (původně COMP128-1, později COMP128-2 nebo COMP128-3) namísto přímého použití nezpracovaného Ki. Když se UE pokouší zaregistrovat v síti využívající podsítě sítě, síť (konkrétně AuC) identifikuje příslušný NSCI, odvodí odpovídající NSCK a poté tento NSCK použije ke generování autentizační trojice ([RAND](/mobilnisite/slovnik/rand/), [SRES](/mobilnisite/slovnik/sres/), Kc). Tato trojice je odeslána do Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) k výzvě pro UE. SIM karta UE provede stejné odvození: pomocí svého uloženého Ki a NSCI (který může být vysílán sítí nebo uložen na SIM kartě) odvodí stejný NSCK a použije ho k výpočtu očekávané odpovědi (SRES) na výzvu sítě (RAND).

Tato architektura umožňuje oddělení klíčů. Různé podsítě sítě používají různé hodnoty NSCI, což vede k odvození různých NSCK ze stejného kořenového Ki. To znamená, že pokud je odvozený NSCK kompromitován v jedné podsíti sítě (např. v síti roamingového partnera), kořenový Ki a klíče používané v jiných podsítích zůstanou chráněny. Poskytovalo to základní formu kryptografického oddělení sítí. Mechanismus NSCK byl součástí vývoje bezpečnostního rámce GSM pro řešení problémů bezpečnosti roamingu a nabízel operátorům větší kontrolu nad používáním klíčů v různých částech jejich sítě nebo u různých partnerů. Jeho role je zcela v rámci domén jádrové sítě s přepojováním okruhů a rané GPRS, rozhraní mezi AuC, HLR a SIM kartou.

## K čemu slouží

NSCK byl vyvinut pro řešení specifických bezpečnostních a provozních omezení původního návrhu zabezpečení GSM, který pro všechna autentizační události všude přímo používal účastníkův Ki. To představovalo dva hlavní problémy. Za prvé, vytvářelo to jediný bod selhání: pokud byl Ki kompromitován v jedné části sítě (např. v AuC roamingového partnera), bezpečnost účastníka byla kompromitována globálně. Za druhé, nenabízelo žádné kryptografické oddělení mezi různými doménami služeb nebo roamingovými partnery v ekosystému operátora. Operátoři požadovali způsob, jak omezit vystavení kořenového klíče (Ki).

Zavedení konceptu Podsítě sítě a NSCK tyto problémy vyřešilo zavedením vrstvy nepřímosti. Kořenový Ki nikdy neopouští zabezpečené AuC domácího operátora. Místo toho se pro vytvoření odvozených klíčů (NSCK) pro použití v konkrétních kontextech používají identifikátory podsítě sítě (NSCI) definované operátorem. To umožnilo operátorovi vydat roamingovému partnerovi pro ověřování v síti tohoto partnera jiný odvozený klíč, aniž by odhalil hlavní Ki. Pokud by došlo k narušení systémů tohoto roamingového partnera, byl by odhalen pouze NSCK pro tuto podsíť a domácí operátor mohl tuto konkrétní podsíť zneplatnit změnou NSCI, aniž by bylo nutné vyměnit SIM kartu nebo kořenový Ki. To poskytlo lepší kontrolu a zmírnilo riziko ve stále složitějším globálním roamingovém prostředí sítí 2G a raných 3G. Představovalo to raný krok k podrobnější správě klíčů, princip, který je rozsáhle rozvíjen v 3G (UMTS) a 4G (LTE) s jejich hierarchií kryptografických klíčů.

## Klíčové vlastnosti

- Odvozený kryptografický klíč, nikoli primární kořenový klíč.
- Generován funkcí pro odvozování klíčů (KDF) pomocí účastníkova Ki a identifikátoru podsítě sítě (NSCI).
- Umožňuje použití různých autentizačních klíčů pro různé podsítě sítě nebo roamingové partnery.
- Chrání kořenový Ki před vystavením v navštívených nebo partnerských sítích.
- Používá se jako vstupní klíč pro GSM autentizační algoritmy (varianty COMP128) k generování autentizačních trojic.
- Umožňuje nezávislé zneplatnění kompromitované podsítě sítě bez ovlivnění hlavní identity účastníka.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G

---

📖 **Anglický originál a plná specifikace:** [NSCK na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsck/)
