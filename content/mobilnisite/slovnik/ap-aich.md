---
slug: "ap-aich"
url: "/mobilnisite/slovnik/ap-aich/"
type: "slovnik"
title: "AP-AICH – Access Preamble Acquisition Indicator Channel"
date: 2025-01-01
abbr: "AP-AICH"
fullName: "Access Preamble Acquisition Indicator Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ap-aich/"
summary: "Downlinkový fyzický kanál v UMTS používaný k potvrzení detekce přístupového preambule (Access Preamble) odeslaného UE na PRACH. Poskytuje UE okamžitou zpětnou vazbu, která indikuje, zda základnová sta"
---

AP-AICH je downlinkový fyzický kanál v UMTS, který potvrzuje detekci přístupového preambule (Access Preamble) od UE na PRACH a poskytuje okamžitou zpětnou vazbu pro proceduru náhodného přístupu.

## Popis

Access Preamble Acquisition Indicator Channel (AP-AICH) je vyhrazený downlinkový fyzický kanál specifikovaný pro režim UTRA [FDD](/mobilnisite/slovnik/fdd/) v UMTS. Funguje v rámci fyzické vrstvy WCDMA definované ve specifikacích 3GPP Release 4 a novějších. AP-AICH vysílá Node B (základnová stanice) a je neodmyslitelně spojen s procedurou na Physical Random Access Channel (PRACH). Jeho primární funkcí je poskytnout rychlý a spolehlivý mechanismus potvrzení pro přístupové preambule odesílané uživatelským zařízením (UE), které se pokouší navázat počáteční spojení nebo požádat o zdroje na uplinku.

Architektonicky je AP-AICH namapován na specifický kanalizační kód a je vysílán v rámci časové struktury primárního Common Control Physical Channel ([P-CCPCH](/mobilnisite/slovnik/p-ccpch/)), přičemž využívá vlastní vyhrazený kanalizační kód v rámci downlinkového scrambling kódu buňky. Nepřenáší transportní bloky ani informace vyšších vrstev; místo toho vysílá jednoduchý signaturní vzor – sekvenci 16 symbolů – který přímo odpovídá signatuře použité UE v jejím vyslaném přístupovém preambuli na PRACH. Kanál je vysílán po dobu 5120 čipů (jeden přístupový slot, Access Slot) synchronizovaně s načasováním přístupových slotů PRACH. Node B zpracovává přijatá preambule z PRACH jejich korelací se známými signaturami. Po úspěšné detekci překračující určitou prahovou hodnotu okamžitě vysílá odpovídající signaturní vzor na AP-AICH.

Tato operace je kritickou součástí procedury náhodného přístupu založené na Slotted ALOHA. UE, která si přeje získat přístup k síti, nejprve vybere Access Service Class ([ASC](/mobilnisite/slovnik/asc/)) a dostupný zdroj PRACH. Poté vysílá sérii postupně silnějších přístupových preambulí (preamble ramping), z nichž každá se skládá ze signatury preambule o délce 4096 čipů zopakované 256krát. Po každém vyslání preambule UE monitoruje AP-AICH během specifického reakčního okna. Pokud na AP-AICH detekuje svou přiřazenou signaturu, interpretuje to jako pozitivní potvrzení ([AI](/mobilnisite/slovnik/ai/)) a pokračuje ve vysílání zprávové části (RACH Message) na PRACH. Pokud potvrzení nepřijme, zvýší výkon preambule a opakuje vysílání po backoff periodě. Tento handshake minimalizuje kolize a zajišťuje, že zprávová část je odeslána pouze tehdy, když je uplink efektivně zachycen.

Role AP-AICH je zásadní pro dostupnost a efektivitu sítě. Poskytnutím okamžité zpětné vazby významně snižuje čas potřebný pro UE k získání synchronizace na uplinku a odeslání své RACH zprávy, což přímo ovlivňuje dobu navazování hovoru a latenci paketových dat. Jeho návrh je optimalizován pro nízkou latenci a vysokou spolehlivost v rámci omezení fyzické vrstvy WCDMA, využívá jednoduchou robustní modulaci ([BPSK](/mobilnisite/slovnik/bpsk/) pro signaturu) pro zajištění jasné detekce i na okraji buňky. Kanál funguje ve spojení s Acquisition Indicator Channel ([AICH](/mobilnisite/slovnik/aich/)), který slouží podobnému účelu pro jiné fyzické kanály, ale AP-AICH je specificky vyhrazen pro proces zachycení preambule na PRACH, což zdůrazňuje důležitost efektivního náhodného přístupu v návrhu systému UMTS.

## K čemu slouží

AP-AICH byl vytvořen k řešení základního problému efektivního a na kolize odolného náhodného přístupu v asynchronních [CDMA](/mobilnisite/slovnik/cdma/) systémech, jako je UMTS WCDMA. V dřívějších mobilních systémech procedury náhodného přístupu často spoléhaly na kontenční metody bez okamžité zpětné vazby, což vedlo k vyšší pravděpodobnosti kolizí, opakovaným přenosům a zvýšené přístupové latenci a spotřebě energie. Návrh UMTS vyžadoval mechanismus, který by umožnil UE rychle a spolehlivě získat uplink a signalizovat svou žádost o vysílání, aniž by způsobovalo nadměrný interference nebo plýtvalo zdroji.

Primární motivací bylo umožnit řízený a energeticky efektivní handshake před vysláním vlastní RACH zprávy. Bez AP-AICH by muselo UE slepě vyslat celou svou zprávu po preambuli, riskujíc kolizi s jinými UE nebo selhání z důvodu nedostatečného výkonu, čímž by plýtvalo kapacitou uplinku a životností baterie. AP-AICH poskytuje uzavřenou smyčku řízení: Node B, který má globální přehled o interferenci na uplinku a přijatých preambulích, může explicitně potvrdit úspěšně detekované preambule. To informuje UE, že uplink je zachycen na dostatečné úrovni výkonu a že může bezpečně pokračovat v přenosu zprávy. Tím se snižuje celková systémová interference, zvyšuje pravděpodobnost úspěšného přístupu a minimalizuje latence při navazování spojení.

Historicky tento přístup zdokonalil koncepty náhodného přístupu z dřívějších systémů GSM a IS-95 a přizpůsobil je jedinečným výzvám širokopásmového CDMA. AP-AICH, zavedený v Release 4 jako součást zralých specifikací UTRA, upevnil tento efektivní mechanismus preambule a potvrzení jako klíčovou součást fyzické vrstvy UMTS. Vyřešil omezení čistě kontenčních nebo otevřených smyček přístupu zavedením rychlé signalizace na první vrstvě, což je nezbytné pro podporu jak hlasových služeb, tak nově se objevujících paketově orientovaných datových služeb s nízkými požadavky na latenci.

## Klíčové vlastnosti

- Poskytuje okamžité potvrzení na fyzické vrstvě pro detekovaná přístupová preambule na PRACH.
- Vysílá 16-symbolový signaturní vzor odpovídající signatuře preambule vyslané UE.
- Funguje s pevným časovým vztahem synchronizovaným k přístupovým slotům PRACH (dobou trvání 5120 čipů).
- Používá BPSK modulaci pro robustní detekci indikátoru zachycení (Acquisition Indicator).
- Umožňuje uzavřenou smyčku řízení výkonu pro proceduru postupného zvyšování výkonu preambule (preamble ramping) před vysláním zprávy.
- Snižuje pravděpodobnost kolizí při náhodném přístupu a celkovou interferenci na uplinku.

## Související pojmy

- [AICH – Acquisition Indication Channel](/mobilnisite/slovnik/aich/)

## Definující specifikace

- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels

---

📖 **Anglický originál a plná specifikace:** [AP-AICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ap-aich/)
