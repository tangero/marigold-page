---
slug: "llgmm"
url: "/mobilnisite/slovnik/llgmm/"
type: "slovnik"
title: "LLGMM – LLC to GPRS Mobility Management service access point"
date: 2025-01-01
abbr: "LLGMM"
fullName: "LLC to GPRS Mobility Management service access point"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/llgmm/"
summary: "LLGMM je konkrétní služební přístupový bod (SAP) mezi vrstvou LLC a podsložkou GMM v GPRS/UMTS. Poskytuje rozhraní pro přenos signalizačních zpráv správy mobility GPRS přes spolehlivý spoj LLC. Zajišť"
---

LLGMM je služební přístupový bod (Service Access Point) mezi vrstvou LLC a podsložkou GMM, který poskytuje rozhraní pro přenos signalizačních zpráv správy mobility GPRS přes spolehlivý spoj LLC.

## Popis

LLGMM ([LLC](/mobilnisite/slovnik/llc/) to [GPRS](/mobilnisite/slovnik/gprs/) Mobility Management service access point) je přesně definovaný logický bod propojení mezi vrstvou řízení logického spoje (Logical Link Control, LLC) a podsložkou správy mobility GPRS (GPRS Mobility Management, [GMM](/mobilnisite/slovnik/gmm/)) v rámci protokolového zásobníku mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) a uzlu SGSN (Serving GPRS Support Node). Je jedním z několika služebních přístupových bodů (SAP) definovaných pro vrstvu LLC, z nichž každý je identifikován identifikátorem služebního přístupového bodu (SAPI). Identifikátor LLGMM-SAPI je výhradně vyhrazen pro signalizační zprávy související s procedurami GMM. Tento SAP funguje jako kanál: podsložka GMM předává své protokolové datové jednotky (PDU) směrem dolů k vrstvě LLC prostřednictvím SAP LLGMM pro přenos a vrstva LLC doručuje příchozí GMM PDU směrem vzhůru přes tentýž SAP.

Provoz zahrnuje to, že vrstva LLC poskytuje pro SAP LLGMM spolehlivý logický spoj v potvrzovaném režimu (acknowledged mode). To je zásadní, protože signalizace GMM zahrnuje kritické procedury, jako je připojení a odpojení k/od GPRS (attach/detach), aktualizace směrovací oblasti, autentizace, vytváření šifrovacích klíčů a žádosti o službu. Tyto zprávy musí být doručeny bezpečně a ve správném pořadí, aby byla zachována registrace v síti, zabezpečení a sledování mobility. Vrstva LLC pro datový proud LLGMM nezávisle na uživatelských datových proudech (které používají jiné SAP, např. LLC-SAPI) zajišťuje segmentaci (je-li potřeba), šifrování pomocí šifrovacího klíče GPRS (je-li šifrování aktivováno), číslování sekvencí, opravu chyb pomocí retransmisí a řízení toku.

V mobilní stanici podsložka GMM generuje signalizační zprávy, jako je ATTACH REQUEST nebo ROUTING AREA UPDATE REQUEST. Ty jsou předány jako služební datové jednotky (SDU) LLC vrstvě LLC prostřednictvím SAP LLGMM. Vrstva LLC vytvoří rámec LLC s příslušnou hodnotou SAPI pro LLGMM, zpracuje jej (včetně případného šifrování) a předá jej vrstvě RLC/[MAC](/mobilnisite/slovnik/mac/) pro rádiový přenos. V SGSN probíhá opačný proces: vrstva LLC přijme rámec, dešifruje jej, ověří čísla sekvencí a doručí GMM PDU entitě GMM v SGSN prostřednictvím SAP LLGMM. Toto oddělení SAP pro signalizaci a uživatelská data umožňuje jejich nezávislou správu a stanovení priority; například signalizaci lze přiřadit vyšší prioritu nebo odlišná nastavení spolehlivosti.

## K čemu slouží

SAP LLGMM byl definován za účelem vytvoření čistého, standardizovaného rozhraní pro přenos signalizace správy mobility [GPRS](/mobilnisite/slovnik/gprs/) přes paketovou doménu. V raném GSM využívala správa mobility pro služby s přepojováním okruhů odlišné kanály a protokoly. Se zavedením GPRS byl pro mobilitu v paketových datech potřebný vyhrazený, spolehlivý signalizační kanál, oddělený od uživatelských dat, aby bylo zajištěno robustní připojení k síti, zabezpečení a správa polohy.

Jeho zavedení řeší problém multiplexování různých typů provozu (signalizace vs. uživatelská data) přes stejný logický spoj při současném uplatnění vhodného zacházení s každým z nich. Přiřazením konkrétního SAPI pro [GMM](/mobilnisite/slovnik/gmm/) může síť použít odlišné provozní režimy [LLC](/mobilnisite/slovnik/llc/) (pro LLGMM je povinný potvrzovaný režim) a potenciálně různé šifrovací kontexty. Toto oddělení zvyšuje bezpečnost, protože signalizační zprávy pro autentizaci a dohodu klíčů jsou chráněny, a zlepšuje spolehlivost, neboť zajišťuje správné zpracování událostí mobility i za špatných rádiových podmínek díky retransmisím na vrstvě LLC.

Historicky, bez vyhrazeného SAP jako je LLGMM, by se signalizace mohla míchat s uživatelskými daty, což by vedlo k potenciálním konfliktům v požadavcích na spolehlivost a ke zpracovatelským zpožděním. SAP LLGMM umožňuje efektivní zpracování procedur mobility, které jsou časově citlivé pro udržení registrace a zajištění plynulého přenosu mobility. Je to základní prvek, který podporuje klíčové funkce GPRS/UMTS, jako jsou aktualizace směrovací oblasti mezi SGSN, kde je integrita signalizace prvořadá pro přenos kontextu mobilního zařízení mezi síťovými uzly bez přerušení služby.

## Klíčové vlastnosti

- Definuje rozhraní pro signalizaci GMM mezi vrstvami LLC a GMM
- Používá specifický identifikátor služebního přístupového bodu (SAPI) vyhrazený pro GMM
- Funguje výhradně v potvrzovaném režimu (acknowledged mode) vrstvy LLC pro spolehlivost
- Podporuje šifrování signalizačních zpráv GMM pro zabezpečení
- Umožňuje nezávislé zpracování oproti tokům uživatelských dat
- Nezbytný pro procedury jako připojení k síti (attach), aktualizace směrovací oblasti a řízení zabezpečení

## Související pojmy

- [GMM – Global Multimedia Mobility](/mobilnisite/slovnik/gmm/)
- [LLC – SM Low Layer Source Specific Multicast (address)](/mobilnisite/slovnik/llc/)
- [LLE – Logical Link Entity](/mobilnisite/slovnik/lle/)

## Definující specifikace

- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [LLGMM na 3GPP Explorer](https://3gpp-explorer.com/glossary/llgmm/)
