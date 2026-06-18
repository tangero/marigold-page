---
slug: "esrn"
url: "/mobilnisite/slovnik/esrn/"
type: "slovnik"
title: "ESRN – Emergency Service Routing Number"
date: 2025-01-01
abbr: "ESRN"
fullName: "Emergency Service Routing Number"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/esrn/"
summary: "Globálně jednoznačné číslo používané k směrování tísňových hovorů k příslušnému přijímacímu středisku tísňového volání (PSAP). Je to kritická součást tísňových služeb IP multimedia subsystému (IMS), k"
---

ESRN je globálně jednoznačné číslo používané k směrování tísňových hovorů k příslušnému přijímacímu středisku tísňového volání (PSAP) v rámci tísňových služeb IMS.

## Popis

Emergency Service Routing Number (ESRN) je standardizovaný identifikátor v architektuře tísňových hovorů 3GPP IMS. Funguje jako směrovací klíč v jádru sítě, který směruje žádost o tísňovou relaci ke správné funkci řízení tísňových hí ([E-CSCF](/mobilnisite/slovnik/e-cscf/)). E-CSCF je uzel IMS odpovědný za zpracování tísňových hovorů. ESRN není vytočeno uživatelem; místo toho je odvozeno síťovými prvky na základě polohy volajícího. Když uživatelské zařízení (UE) zahájí tísňový hovor, Proxy-CSCF ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) detekuje žádost o tísňovou relaci. P-CSCF následně dotazuje funkci získávání polohy ([LRF](/mobilnisite/slovnik/lrf/)), aby získala jak směrovací informace (ESRN), tak informace o poloze volajícího (Emergency Service Query Key, [ESQK](/mobilnisite/slovnik/esqk/)). LRF určuje příslušnou jurisdikci [PSAP](/mobilnisite/slovnik/psap/) na základě poskytnuté nebo odhadované polohy UE.

Po získání zahrne P-CSCF ESRN do parametru Request-URI žádosti [SIP](/mobilnisite/slovnik/sip/) INVITE při předávání hovoru k E-CSCF. ESRN slouží jako token, který E-CSCF sděluje, ke kterému konkrétnímu bránovému PSAP nebo funkci hraniční kontroly ([BCF](/mobilnisite/slovnik/bcf/)) by měl být hovor směrován. E-CSCF používá ESRN k výběru správného výstupního trunku nebo rozhraní směrem k síti PSAP. Tento mechanismus odděluje komplexní logiku směrování na základě polohy (zpracovávanou LRF) od základního směrování relací prováděného [CSCF](/mobilnisite/slovnik/cscf/). Architektura zajišťuje, že jádrová síť IMS nemusí udržovat podrobné mapy hranic PSAP v reálném čase.

Spolu s ESRN je E-CSCF poskytnut také ESQK, který je nakonec doručen PSAP. PSAP může použít ESQK v následném zpětném volání k LRF k získání přesné polohy volajícího. Tento systém dvou čísel (ESRN pro směrování, ESQK pro získání polohy) je základním kamenem tísňových služeb IMS. ESRN je definováno jako globálně jednoznačné, typicky ve formátu čísla E.164, aby se předešlo konfliktům a zajistilo jednoznačné směrování napříč různými síťovými operátory a zeměmi. Jeho implementace je podrobně popsána v 3GPP TS 23.167, která specifikuje celkovou architekturu a procedury pro tísňové relace IMS.

## K čemu slouží

ESRN bylo vytvořeno k vyřešení kritického problému směrování tísňových hovorů v plně IP sítích, jako je IMS, kde tradiční metody v přepojovaných okruzích založené na vytočených číslicích (např. 911, 112) jsou nedostatečné. V legacy sítích byly tísňové hovory směrovány na základě základnové stanice nebo ústředny obsluhující volajícího. IMS zavádí mobilitu, nomadický přístup a služby Voice over IP (VoIP), kde IP adresa uživatele nebo bod připojení k síti spolehlivě neindikuje jeho fyzickou polohu pro účely tísňového volání. Primárním problémem je zajistit, aby tísňový hovor dospěl k PSAP odpovědnému za aktuální zeměpisnou oblast volajícího, bez ohledu na jeho domovskou síť nebo stav předplatného.

Motivace vycházela z regulatorních požadavků na poskytování spolehlivých tísňových služeb v sítích nové generace (NGN). Předchozí přístupy postrádaly standardizovaný, škálovatelný mechanismus pro dynamické směrování na základě polohy v dekomponované, službami řízené architektuře. ESRN ve spojení s LRF tento mechanismus poskytuje. Umožňuje, aby rozhodnutí o směrování bylo založeno na nejpřesnější dostupné poloze (občanská adresa, geodetické souřadnice) spíše než na topologii sítě, což je zásadní pro VoIP hovory z notebooků, pevných bezdrátových terminálů nebo návštěvních uživatelů.

Řeší omezení, které by vyžadovalo, aby každý CSCF měl úplné tabulky směrování PSAP. Centralizací rozhodnutí o směrování v LRF a předáním jednoduchého tokenu (ESRN) se systém stává škálovatelnějším, udržovatelnějším a přizpůsobivějším změnám v jurisdikcích PSAP. Také usnadňuje propojení mezi různými síťovými operátory a infrastrukturami PSAP tím, že poskytuje standardizované číslo pro účely směrování.

## Klíčové vlastnosti

- Globálně jednoznačné číslo ve stylu E.164 pro jednoznačné síťové směrování
- Dynamicky přidělováno funkcí získávání polohy (LRF) na základě polohy volajícího
- Používáno jako hodnota Request-URI pro směrování SIP INVITE k Emergency-CSCF (E-CSCF)
- Odděluje komplexní výběr PSAP na základě polohy od základních funkcí řízení relací
- Umožňuje směrování tísňových hovorů pro neautentizované, roamující nebo uživatele bez předplatného
- Funguje v tandemu s klíčem pro dotaz na tísňovou službu (ESQK) pro získání polohy

## Související pojmy

- [E-CSCF – Emergency – Call Session Control Function](/mobilnisite/slovnik/e-cscf/)

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions

---

📖 **Anglický originál a plná specifikace:** [ESRN na 3GPP Explorer](https://3gpp-explorer.com/glossary/esrn/)
