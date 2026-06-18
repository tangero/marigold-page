---
slug: "cbra"
url: "/mobilnisite/slovnik/cbra/"
type: "slovnik"
title: "CBRA – Contention Based Random Access"
date: 2025-01-01
abbr: "CBRA"
fullName: "Contention Based Random Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cbra/"
summary: "CBRA je procedura náhodného přístupu v 5G NR, při které může více uživatelských zařízení (UE) usilovat o počáteční přístup k síti nebo synchronizaci v uplinku vysíláním na stejném zdroji preambule, co"
---

CBRA (Contention Based Random Access) je procedura náhodného přístupu v 5G NR, při které může více uživatelských zařízení (UE) usilovat o přístup vysíláním na stejném zdroji preambule, což umožňuje efektivní počáteční přístup a resynchronizaci v uplinku i přes možnou kolizi.

## Popis

Contention Based Random Access (CBRA) je základní procedura v rámci 5G New Radio (NR) Radio Access Network (RAN) definovaná standardy 3GPP. Umožňuje uživatelskému zařízení (UE) zahájit komunikaci s gNodeB (gNB), když nemá vyhrazený zdroj pro uplink nebo přesné časové zarovnání pro uplink. Procedura je označována jako 'contention-based' (založená na kolizi), protože více UE může současně vybrat a vyslat stejnou preambuli pro náhodný přístup na sdíleném zdroji fyzického kanálu pro náhodný přístup ([PRACH](/mobilnisite/slovnik/prach/)), což vede ke scénáři kolize, který musí být vyřešen. CBRA je primárně spouštěna pro události jako počáteční přístup ze stavů [RRC](/mobilnisite/slovnik/rrc/)_IDLE nebo RRC_INACTIVE, obnovení RRC spojení, předání (handover), příchod dat v uplinku při ztrátě synchronizace a obnovení po selhání žádosti o naplánování (scheduling request).

Procedura CBRA následuje dobře definovanou čtyřkrokovou výměnu zpráv, často označovanou jako 4-step [RACH](/mobilnisite/slovnik/rach/). V kroku 1 (Msg1) UE vybere preambuli pro náhodný přístup ze sady preambulí pro CBRA nakonfigurovaných gNB prostřednictvím systémové informace a vyšle ji na časově-frekvenčním zdroji PRACH. Preambule slouží jako podpis a umožňuje gNB odhadnout časový posun (timing advance) UE. V kroku 2 (Msg2) gNB odpoví zprávou Random Access Response ([RAR](/mobilnisite/slovnik/rar/)) na [PDSCH](/mobilnisite/slovnik/pdsch/), adresovanou pomocí dočasného identifikátoru Random Access Radio Network Temporary Identifier ([RA-RNTI](/mobilnisite/slovnik/ra-rnti/)). RAR přenáší povolení pro uplink (uplink grant) pro Msg3, dočasný Cell Radio Network Temporary Identifier (TC-RNTI) pro UE a příkaz pro časový posun (timing advance command).

Po přijetí platné RAR pokračuje UE krokem 3 (Msg3). Pomocí přiděleného zdroje pro uplink vysílá UE RRC zprávu (např. RRCSetupRequest, RRCResumeRequest), která obsahuje jedinečný identifikátor UE, jako je Resume ID nebo náhodná hodnota. Tento krok je klíčový pro řešení kolizí. Protože více UE mohlo použít stejnou preambuli a obdržet stejný TC-RNTI a povolení, jejich přenosy Msg3 se srazí (kolize). gNB úspěšně dekóduje jednu Msg3 a předá ji vyšším vrstvám. Nakonec, v kroku 4 (Msg4), gNB odešle zprávu pro řešení kolizí (Contention Resolution message) adresovanou UE pomocí jedinečného identifikátoru z Msg3 (např. prostřednictvím [C-RNTI](/mobilnisite/slovnik/c-rnti/) nebo ozvěnou identity UE v [MAC](/mobilnisite/slovnik/mac/) CE). Pouze UE, jejíž identifikátor odpovídá, považuje proceduru za úspěšnou, prohlásí TC-RNTI za své C-RNTI a pokračuje. Ostatní konkurenční UE detekují selhání, provedou čekání (backoff) a opakují pokus.

Architektura podporující CBRA zahrnuje MAC a PHY vrstvy UE, MAC a PHY vrstvy gNB a signalizaci vrstvy RRC. Klíčové komponenty fyzické vrstvy zahrnují konfiguraci PRACH (formát preambule, časové/frekvenční zdroje), PDCCH pro plánování RAR (pomocí RA-RNTI odvozeného od PRACH okamžiku) a PUSCH/PDSCH pro přenos Msg3 a Msg4. Role procedury je klíčová pro vstup do sítě, obnovení synchronizace v uplinku a správu spojení, čímž tvoří základ spolehlivého a efektivního počátečního přístupu v 5G sítích. Její návrh vyvažuje efektivitu využití zdrojů pro scénáře masivního připojení s potřebou robustního řešení kolizí.

## K čemu slouží

CBRA existuje, aby poskytla škálovatelný a efektivní mechanismus pro uživatelská zařízení (UE), jak získat počáteční synchronizaci v uplinku a požádat o zdroje od sítě bez předchozí koordinace plánování. V celulárních systémech nemůže UE jednoduše začít vysílat data; musí nejprve zarovnat svůj časový posun (timing advance) pro uplink s gNB, aby předešla interferencím, a musí jí být přiděleny rádiové zdroje. Procedura náhodného přístupu řeší tento problém typu 'slepice a vejce'. Přístup založený na kolizi je motivován sporadickou a nepředvídatelnou povahou pokusů o přístup od potenciálně velkého počtu UE, což znemožňuje přiřazovat vyhrazené zdroje pro každý potenciální přístup. CBRA umožňuje síti obsloužit mnoho UE s omezenou sadou zdrojů pro preambule, přičemž příležitostné kolize přijímá jako kompromis za sníženou signalizační režii a rezervaci zdrojů.

Historicky byl contention-based random access základním kamenem celulárních systémů již od GSM (s jeho RACH) přes UMTS až po LTE. Každá generace proceduru zdokonalovala pro nižší latenci a vyšší spolehlivost. V 5G NR řeší CBRA omezení předchozích přístupů podporou širší škály případů užití, včetně rozšířeného mobilního širokopásmového připojení (eMBB), ultra-spolehlivé komunikace s nízkou latencí (URLLC) a masivní komunikace mezi stroji (mMTC). Pro mMTC je klíčovou výzvou zvládání masivního počtu zařízení pokoušejících se o přístup současně, což CBRA řeší prostřednictvím funkcí jako vylepšené čekání (enhanced backoff) a flexibilní konfigurace zdrojů PRACH. Ve srovnání se svým protějškem Contention-Free Random Access (CFRA), který používá vyhrazené preambule přiřazené gNB pro konkrétní UE (např. během předání), je CBRA hlavním nástrojem pro neplánované scénáře počátečního přístupu. Její vytvoření a standardizace v 3GPP Rel-15 bylo hnací silou potřeby flexibilního, robustního a efektivního přístupového schématu schopného podporovat rozmanité požadavky 5G, od vysokorychlostních smartphonů po nízkopříkonové IoT senzory.

## Klíčové vlastnosti

- Využívá čtyřkrokovou výměnu zpráv (Msg1/Msg2/Msg3/Msg4) pro robustní řešení kolizí
- Používá preambule pro přístup s kolizemi (contention-based), vysílané na sdílených zdrojích PRACH
- Zahrnuje mechanismus řešení kolizí (Contention Resolution) založený na jedinečných identifikátorech UE v Msg3/Msg4
- Podporuje flexibilní konfiguraci PRACH pro různá nasazení a případy užití (např. různá rozteč podnosných)
- Obsahuje mechanismus čekání (backoff) pro řízení časování retransmisí po kolizních selháních
- Umožňuje počáteční odhad časového posunu (timing advance) a synchronizaci v uplinku pro UE

## Související pojmy

- [CFRA – Contention Free Random Access](/mobilnisite/slovnik/cfra/)
- [PRACH – Physical Random Access Channel](/mobilnisite/slovnik/prach/)
- [RAR – Re-Auth-Request](/mobilnisite/slovnik/rar/)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.391** (Rel-19) — NR; Ambient IoT MAC Protocol Spec
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [CBRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbra/)
