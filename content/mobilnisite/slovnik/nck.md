---
slug: "nck"
url: "/mobilnisite/slovnik/nck/"
type: "slovnik"
title: "NCK – Network Control Key"
date: 2025-01-01
abbr: "NCK"
fullName: "Network Control Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nck/"
summary: "Kryptografický klíč používaný v sítích GSM a UMTS k autentizaci sítě vůči mobilnímu zařízení a zabezpečení signalizace. Je součástí autentizačního kvintetu, je odvozen spolu se šifrovacím klíčem a zaj"
---

NCK (Network Control Key) je klíč pro řízení sítě, kryptografický klíč používaný v sítích GSM a UMTS k autentizaci sítě vůči mobilnímu zařízení a zabezpečení signalizace, který chrání před útoky falešných základnových stanic.

## Popis

Klíč pro řízení sítě (NCK) je základní bezpečnostní klíč v mobilních sítích 2G (GSM) a 3G (UMTS), definovaný ve standardech 3GPP. Jedná se o 128bitový kryptografický klíč, který tvoří část autentizačního vektoru (konkrétně kvintetu v GSM nebo v raných kontextech UMTS), generovaného autentizačním centrem (AuC) v domovské síti. NCK je odvozen během procesu autentizace a dohody o klíči ([AKA](/mobilnisite/slovnik/aka/)) za použití sdíleného tajného klíče (Ki) uloženého v [SIM](/mobilnisite/slovnik/sim/)/[USIM](/mobilnisite/slovnik/usim/) účastníka a v AuC spolu s náhodnou výzvou ([RAND](/mobilnisite/slovnik/rand/)). Primární funkcí NCK je poskytnout mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelskému zařízení (UE) prostředek k ověření autenticity obsluhující sítě, což je proces známý jako autentizace sítě. Ten se liší od autentizace uživatele, která používá podepsanou odpověď ([SRES](/mobilnisite/slovnik/sres/)) nebo autentizační token ([AUTN](/mobilnisite/slovnik/autn/)).

Při provozu, když se UE připojí k síti, navštívená nebo obsluhující síť požádá o autentizační vektory z AuC domovské sítě. AuC vygeneruje RAND a pomocí Ki a algoritmů (např. COMP128 pro GSM, MILENAGE pro UMTS/LTE) vypočítá sadu klíčů včetně NCK, šifrovacího klíče (Kc pro GSM, [CK](/mobilnisite/slovnik/ck/) pro UMTS) a integritního klíče (IK pro UMTS) spolu s očekávanou odpovědí (SRES/XRES) a autentizačním tokenem (AUTN). NCK je bezpečně odeslán do obsluhující sítě (např. VLR/SGSN) v rámci autentizačního vektoru. Síť následně použije NCK v následných bezpečnostních procedurách k prokázání své legitimity vůči UE, typicky vygenerováním síťového autentizačního tokenu. UE, které disponuje stejným Ki a RAND, nezávisle vypočítá NCK a ověří token. Tato vzájemná autentizace zabraňuje útokům falešných základnových stanic (rogue BTS).

Z architektonického hlediska je NCK součástí hierarchie klíčů zakořeněné v dlouhodobém tajemství Ki. Používá se výhradně pro autentizaci na straně sítě a nepoužívá se pro šifrování nebo ochranu integrity uživatelských dat – tyto funkce zajišťují klíče Kc, CK nebo IK. V pozdějších vydáních 3GPP se tento koncept vyvinul v propracovanější hierarchie klíčů v LTE a 5G, kde klíče jako KASME a z nich odvozené klíče poskytují podobné funkce vzájemné autentizace, ale NCK zůstává specifický pro bezpečnostní architektury GSM a UMTS. Jeho role je klíčová pro zajištění, že se UE připojí pouze k legitimní síti, čímž chrání účastníky před odposlechem a útoky typu man-in-the-middle uskutečňovanými prostřednictvím nelegitimního síťového zařízení.

## K čemu slouží

NCK byl zaveden, aby odstranil významnou bezpečnostní slabinu raných mobilních sítí: absenci vzájemné autentizace. V počátečních systémech GSM pouze síť autentizovala uživatele (prostřednictvím SRES), ale uživatel neměl možnost ověřit autenticitu sítě. To činilo účastníky zranitelnými vůči útokům falešných základnových stanic, kdy útočníci mohli nastavit nelegitimní zařízení BTS, aby vydávali za legitimní síť, odposlouchávali hovory nebo sledovali polohu. NCK byl vytvořen jako součást vylepšených bezpečnostních mechanismů v pozdějších fázích GSM a v UMTS, aby umožnil autentizaci sítě, čímž se stanovila vzájemná autentizace mezi UE a sítí.

Tento vývoj byl motivován rostoucí potřebou důvěry v mobilní komunikaci, jak se služby rozšiřovaly z hlasových na datové a vznikající mobilní obchodování. Omezení předchozího přístupu – jednostranné autentizace – představovala rizika pro soukromí a bezpečnost uživatelů. Začleněním NCK do autentizačního vektoru poskytlo 3GPP standardizovanou metodu, jak mohou sítě prokázat svou identitu, a to využitím sdíleného tajemství Ki bez jeho vyzrazení. Tím se posílil celkový bezpečnostní rámec a položily se základy pro pokročilejší hierarchie klíčů a protokoly vzájemné autentizace v UMTS a pozdějších technologiích, což zajišťuje, že obě strany v komunikaci mohou důvěřovat vzájemné identitě.

## Klíčové vlastnosti

- 128bitový kryptografický klíč, součást autentizačních vektorů GSM/UMTS
- Umožňuje autentizaci sítě vůči mobilnímu zařízení
- Odvozen z dlouhodobého tajemství Ki a náhodné výzvy RAND
- Generován autentizačním centrem (AuC) v domovské síti
- Zabraňuje útokům falešných základnových stanic (rogue BTS)
- Používá se v procesu vzájemné autentizace spolu s autentizací uživatele

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G

---

📖 **Anglický originál a plná specifikace:** [NCK na 3GPP Explorer](https://3gpp-explorer.com/glossary/nck/)
