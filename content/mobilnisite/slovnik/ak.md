---
slug: "ak"
url: "/mobilnisite/slovnik/ak/"
type: "slovnik"
title: "AK – Anonymity Key"
date: 2025-01-01
abbr: "AK"
fullName: "Anonymity Key"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ak/"
summary: "Kryptografický klíč používaný v sítích 3GPP k ochraně identity uživatele během autentizačních procedur. Zabrání sledování účastníků tím, že zajistí, že dočasné identity nelze spojit s trvalými identif"
---

AK je kryptografický klíč používaný v sítích 3GPP k ochraně identity uživatele během autentizace tím, že zajišťuje, že dočasné identity nelze spojit s jeho trvalým identifikátorem, čímž zabraňuje sledování účastníka.

## Popis

Anonymity Key (AK, Klíč anonymity) je základní kryptografický prvek v rámci architektury Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) od 3GPP, konkrétně navržený k ochraně soukromí identity uživatele. Je generován Authentication Centre (AuC) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) jako součást procesu generování kvintetu nebo autentizačního vektoru pro 3G UMTS nebo jako součást autentizačního vektoru pro EPS AKA v 4G/LTE a 5G AKA v 5G systémech. AK je odvozen pomocí funkce pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)), která jako vstupy bere trvalý tajný klíč účastníka (K) a náhodnou výzvu (RAND) generovanou sítí. Toto odvození zajišťuje, že AK je jedinečný pro každou instanci autentizace.

Při provozu se AK používá k zakrytí trvalé identity účastníka, International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), když jsou použity dočasné identity jako Temporary Mobile Subscriber Identity (TMSI) v 3G/4G nebo [5G-GUTI](/mobilnisite/slovnik/5g-guti/) v 5G. Během počátečního připojení k síti nebo když nelze ověřit dočasnou identitu, může síť požadovat trvalou identitu. Aby se zabránilo odposlechnutí IMSI v nešifrované podobě, použije se AK k jejímu zašifrování. Konkrétně je IMSI před přenosem přes rozhraní vzduchu vyloučeno s klíčovým proudem generovaným z AK (a často dalších parametrů, jako je pořadové číslo SQN). Pouze legitimní síť, která má stejný AK, to může dešifrovat a získat skutečné IMSI.

Role AK je odlišná od ostatních klíčů v hierarchii AKA, jako je Cipher Key ([CK](/mobilnisite/slovnik/ck/)) a Integrity Key ([IK](/mobilnisite/slovnik/ik/)), které chrání uživatelská data a signalizační zprávy. AK se zaměřuje výhradně na ochranu identity. Jeho síla závisí na náhodnosti RAND a utajení kořenového klíče K. Oddělení funkce anonymity od funkcí důvěrnosti a integrity je klíčovým architektonickým principem, který umožňuje nezávislé hodnocení a potenciální aktualizace algoritmů. V 5G principy zůstávají, ačkoli hierarchie klíčů je rozšířena o kotvící klíč K_[AUSF](/mobilnisite/slovnik/ausf/) a mechanismy ochrany soukromí jsou posíleny v rámci protokolů 5G AKA a EAP-AKA'.

Účinnost mechanismu AK je klíčová pro zmírnění útoků na sledování polohy a zachycení identity účastníka. Tím, že zajišťuje, že trvalá identita není nikdy přenášena v otevřené podobě, řeší významnou zranitelnost v oblasti soukromí přítomnou v raných celulárních systémech. AK je klíčovou součástí pro splnění regulatorních a konstrukčních požadavků 3GPP na soukromí účastníka, což z něj činí nepostradatelný prvek napříč bezpečnostními architekturami UMTS, EPS a 5G System.

## K čemu slouží

Anonymity Key byl zaveden, aby vyřešil kritickou zranitelnost v oblasti soukromí spočívající v zachycení identity účastníka v mobilních sítích. V raných 2G GSM systémech mohlo být IMSI přenášeno v nešifrované podobě během počáteční registrace v síti nebo za určitých chybových stavů, což umožňovalo pasivním odposlouchávačům identifikovat a sledovat účastníky. To představovalo významnou hrozbu pro soukromí, umožňující profilování uživatelů, sledování polohy a cílené útoky. Vytvoření AK jako součásti bezpečnostní architektury 3G UMTS byla přímou reakcí na toto omezení, která od počátku vložila silnou kryptografickou ochranu identity do základního síťového autentizačního protokolu.

Primární problém, který AK řeší, je spojitelnost uživatelských relací a akcí. Bez něj by protivník mohl korelovat dočasné identity s trvalými zachycením počátečního přenosu IMSI v otevřené podobě. AK toto spojení přerušuje tím, že zajišťuje, že trvalá identita je vždy zašifrována, když je nutná pro procedury obnovy. Tento návrh chrání důvěrnost účastníka, což je základní požadavek moderních telekomunikačních standardů a předpisů na ochranu dat, jako je GDPR. Zajišťuje, že i když jsou signalizační zprávy zachyceny, dlouhodobá identita uživatele zůstane před neoprávněnými stranami skryta.

Dále AK podporuje provozní efektivitu sítě. Umožňuje sítím volně používat a přidělovat dočasné identity (TMSI, 5G-GUTI) pro směrování a paging bez ohrožení soukromí. Systém se může zotavit z chyb synchronizace dočasné identity (např. když mobilní zařízení předloží TMSI, které síť již nerozpozná) bezpečným vyžádáním trvalé identity, a to vše při zachování ochrany přes rozhraní vzduchu. AK tedy umožňuje praktickou rovnováhu mezi robustním soukromím a spolehlivým přístupem k síti, což je motivace klíčová pro jeho zařazení a trvání od 3G UMTS (Release 4) přes všechny následující 5G release.

## Klíčové vlastnosti

- Kryptograficky skrývá International Mobile Subscriber Identity (IMSI) během přenosu
- Odvozen z trvalého tajného klíče účastníka (K) a náhodné výzvy (RAND) pomocí funkce pro odvozování klíčů
- Integrální součást autentizačního vektoru generovaného HSS/AuC pro procedury 3G, 4G a 5G AKA
- Umožňuje bezpečné obnovení trvalé identity, když selže rozlišení dočasné identity (TMSI/5G-GUTI)
- Poskytuje oddělení ochrany identity od funkcí důvěrnosti uživatelských dat a integrity signalizace
- Základní pro prevenci sledování účastníků a splnění regulatorních požadavků na soukromí

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [5G-GUTI – 5G Globally Unique Temporary Identifier](/mobilnisite/slovnik/5g-guti/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.105** (Rel-19) — 3G Security: Cryptographic Algorithm Requirements
- **TS 33.220** (Rel-19) — Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)
- **TS 33.221** (Rel-19) — Subscriber Certificate Distribution via GBA
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 35.205** (Rel-19) — MILENAGE Algorithm Set: General Overview
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [AK na 3GPP Explorer](https://3gpp-explorer.com/glossary/ak/)
