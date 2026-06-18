---
slug: "sres"
url: "/mobilnisite/slovnik/sres/"
type: "slovnik"
title: "SRES – Signed RESponse"
date: 2025-01-01
abbr: "SRES"
fullName: "Signed RESponse"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sres/"
summary: "Autentizační hodnota generovaná SIM nebo USIM kartou během 2G Authentication and Key Agreement (AKA). Jedná se o kryptografickou odpověď na síťovou výzvu (RAND), která slouží k ověření identity účastn"
---

SRES je kryptografická autentizační hodnota generovaná SIM nebo USIM kartou v odpovědi na síťovou výzvu za účelem ověření identity účastníka během 2G autentizace.

## Popis

Signed RESponse (SRES) je klíčovou součástí autentizačního mechanismu 2G GSM, konkrétně v rámci algoritmu [A3](/mobilnisite/slovnik/a3/). Proces začíná, když Autentizační centrum (AuC) sítě vygeneruje 128bitové náhodné číslo ([RAND](/mobilnisite/slovnik/rand/)) a odešle jej do mobilní stanice ([MS](/mobilnisite/slovnik/ms/)). [SIM](/mobilnisite/slovnik/sim/) karta v MS přijme tento RAND a pomocí tajného klíče (Ki), který je sdílen pouze mezi SIM a AuC, jej zpracuje algoritmem A3. Tento výpočet vytvoří 32bitový výstup, kterým je SRES. MS odešle tento SRES zpět do sítě. Současně AuC provede identický výpočet pomocí své uložené kopie účastníkova Ki a stejného RANDu, aby vygenerovalo očekávanou hodnotu SRES. Síť porovná přijatý SRES od MS s lokálně vypočítaným očekávaným SRES. Shoda autentizuje účastníka, čímž prokáže, že disponuje správným tajným klíčem, a udělí přístup k síťovým službám. SRES je statické délky, relativně krátká hodnota navržená s ohledem na výpočetní omezení raných SIM karet. Její generování a ověření jsou zásadní pro paradigma výzva-odpověď, které brání útokům typu impersonation tím, že zajišťuje, aby pouze legitimní účastník se správným Ki mohl vytvořit správnou odpověď na unikátní, neopakovatelnou síťovou výzvu. Ačkoli je SRES mechanismus ústřední pro 2G zabezpečení, je součástí sady, která zahrnuje také algoritmus [A8](/mobilnisite/slovnik/a8/) pro generování relací šifrovacího klíče (Kc). Celá autentizační trojice (RAND, SRES, Kc) je odeslána z Home Location Register ([HLR](/mobilnisite/slovnik/hlr/))/AuC do Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN), aby umožnila lokální autentizaci během mobility.

## K čemu slouží

SRES byl vytvořen k zajištění autentizace účastníka v 2G GSM sítích, čímž řešil kritický problém neoprávněného přístupu k síti. Před digitální buněčnou autentizací byly analogové systémy zranitelné vůči klonování a odposlechu. SRES jako součást procedury AKA zavedl kryptografickou metodu založenou na principu výzva-odpověď k ověření, že mobilní stanice je legitimním účastníkem síťového operátora. Řeší potřebu odlehčeného, implementovatelného bezpečnostního mechanismu, který mohl běžet na omezeném hardwaru raných SIM karet, a zároveň poskytoval základní vrstvu důvěry. Motivací bylo překročit jednoduché kontroly identifikátorů (jako Electronic Serial Numbers), které bylo možné zkopírovat, a přejít k systému založenému na sdíleném tajemství (Ki), které nikdy neputuje rádiovým rozhraním. Tím, že SIM prostřednictvím SRES prokázala znalost Ki, mohla síť uživatele s důvěrou autentizovat. Tento návrh zmírnil riziko prostého podvodu a vytvořil základ pro následující robustnější autentizační metody 3G/4G/5G. Jeho účelem však byla primárně autentizace; neposkytoval vzájemnou autentizaci (síť se v 2G účastníkovi neprokazovala) ani silnou ochranu proti aktivním útokům – omezení, která se snažily řešit pozdější generace.

## Klíčové vlastnosti

- 32bitový kryptografický výstup generovaný algoritmem A3.
- Součást protokolu výzva-odpověď využívajícího náhodnou síťovou výzvu (RAND).
- Odvozen od unikátního tajného klíče účastníka (Ki) uloženého na SIM a v AuC.
- Umožňuje jednostrannou autentizaci mobilního účastníka vůči síti.
- Používá se jako jeden prvek autentizační trojice (RAND, SRES, Kc).
- Základní prvek architektury zabezpečení GSM pro řízení přístupu.

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [SIM – Subscriber Identity Module / Universal Subscriber Identity Module](/mobilnisite/slovnik/sim/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [RAND – RANDom number (authentication parameter)](/mobilnisite/slovnik/rand/)
- [AUC – Authentication Centre](/mobilnisite/slovnik/auc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance

---

📖 **Anglický originál a plná specifikace:** [SRES na 3GPP Explorer](https://3gpp-explorer.com/glossary/sres/)
