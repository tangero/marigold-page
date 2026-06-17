---
slug: "hho"
url: "/mobilnisite/slovnik/hho/"
type: "slovnik"
title: "HHO – Hard Handover"
date: 2025-01-01
abbr: "HHO"
fullName: "Hard Handover"
category: "Mobility"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/hho/"
summary: "Hard Handover (HHO, tvrdé předávání) je procedura předávání, při níž je rádiové spojení se současnou buňkou přerušeno dříve, než je navázáno nové spojení s cílovou buňkou. Je charakterizována operací"
---

HHO (tvrdý předávání) je procedura předávání, při níž je rádiové spojení se současnou buňkou přerušeno dříve, než je navázáno nové spojení s cílovou buňkou, což vede ke krátkému přerušení přenosu.

## Popis

Hard Handover (HHO), známé také jako předávání typu „přeruš a pak navaz“ (break-before-make), je základní procedura mobility v celulárních sítích, při níž uživatelské zařízení (UE) přechází spojení z jedné buňky (zdrojové) do druhé (cílové) tak, že se nejprve odpojí od zdrojové buňky a teprve poté naváže spojení s cílovou buňkou. Tento proces inherentně zahrnuje přerušení aktivního rádiového spoje. Předávání je „tvrdé“, protože neexistuje období, během kterého by bylo UE současně připojeno k oběma buňkám. Celý proces – včetně hlášení měření, rozhodování, provedení a obnovení rádiových prostředků – je řízen sítí (předávání řízené sítí).

Technické provedení tvrdého předávání následuje definovanou sekvenci. Nejprve UE na příkaz sítě provádí měření na obsluhující buňce a sousedních buňkách. Tato měření (např. síla signálu, kvalita) jsou hlášena síti. Na základě přednastavených prahových hodnot a algoritmů rozhodne vrstva Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) sítě, že je předávání nutné. Síť následně připraví prostředky v cílové buňce (např. přidělí provozní kanál). Poté odešle zprávu „Handover Command“ (příkaz k předání) do UE, která mu nařídí opustit současný kanál a naladit se na nový kanál v cílové buňce. Po přijetí tohoto příkazu se UE odpojí od zdrojové buňky, synchronizuje se s cílovou buňkou a provede proceduru náhodného přístupu k navázání nového spoje. Nakonec je prostřednictvím nové buňky odeslána do sítě zpráva „Handover Complete“ (předání dokončeno).

Mezi klíčové komponenty patří měřicí jednotka UE, základnová stanice (Node B, eNodeB, gNB) zdrojové i cílové buňky a řídicí síťová entita ([BSC](/mobilnisite/slovnik/bsc/), RNC, nebo v 5G gNB-CU). Doba přerušení, byť krátká (typicky desítky až několik set milisekund), je kritickým výkonnostním metrikem. Během této doby mohou být uživatelské datové pakety ztraceny nebo zpožděny, což může ovlivnit kvalitu služeb v reálném čase, jako jsou hovory nebo streamování videa. Ke zmírnění tohoto efektu lze použít protokoly, jako je přesměrování paketů ze zdrojového do cílového uzlu, ke snížení ztráty dat.

HHO je kontrastováno s měkkým (Soft) a vnitrobuněčným měkkým (Softer) předáváním používaným v systémech založených na [CDMA](/mobilnisite/slovnik/cdma/), jako je UMTS, kde UE během přechodu udržuje současná spojení („navaz a pak přeruš“ – make-before-break). V GSM, LTE a 5G NR (ve většině kmitočtových pásem) je tvrdé předávání standardní procedurou z důvodu povahy technologie rádiového přístupu ([FDMA](/mobilnisite/slovnik/fdma/)/TDMA/[OFDMA](/mobilnisite/slovnik/ofdma/)). V 5G, ačkoli základní princip předávání zůstává, byl optimalizován rychlejším signalizováním a protokolovými zásobníky s duální aktivitou pro minimalizaci doby přerušení, stále však následuje paradigma přeruš a pak navaz.

## K čemu slouží

Hard Handover existuje jako základní metoda pro udržení kontinuity hovoru a relace, když se uživatel pohybuje celulární sítí. Jeho primárním účelem je plynule přenést probíhající komunikační relaci z jedné rádiové buňky do druhé bez zásahu uživatele, čímž umožňuje mobilitu. Přístup „přeruš a pak navaz“ byl nutným konstrukčním rozhodnutím pro rané celulární systémy jako GSM, které používaly vícečetný přístup s dělením kmitočtu ([FDMA](/mobilnisite/slovnik/fdma/)) a času (TDMA). V těchto technologiích se může rádiové zařízení UE naladit vždy pouze na jeden kmitočet/časový slot, což fyzicky brání současnému spojení se dvěma buňkami.

Problémy, které řeší, jsou správa hranic buněk a vyhýbání se rušení. Když se UE pohybuje k okraji buňky, kvalita signálu se zhoršuje. HHO umožňuje síti proaktivně nařídit UE přejít na silnější buňku dříve, než spojení spadne, čímž zlepšuje míru ztráty hovorů a celkovou kvalitu služby. Také umožňuje síti vyvažovat provozní zatížení mezi buňkami a efektivně spravovat rádiové prostředky. Řízení se zaměřením na síť umožňuje optimalizovaná rozhodnutí založená na globálním pohledu na stav sítě.

Zatímco pozdější technologie zavedly měkké předávání pro lepší spolehlivost za cenu větší spotřeby prostředků, HHO zůstalo relevantní díky své jednoduchosti, efektivitě ve využití spektra (neobsazují se současné kanály) a vhodnosti pro rádiová rozhraní nevyužívající [CDMA](/mobilnisite/slovnik/cdma/). Jeho vývoj se zaměřil na minimalizaci inherentní doby přerušení prostřednictvím rychlejší signalizace, lepší synchronizace mezi buňkami a optimalizací protokolů, což zajišťuje jeho životaschopnost i pro aplikace 5G s nízkou latencí.

## Klíčové vlastnosti

- Operace „přeruš a pak navaz“: zdrojové spojení je uvolněno dříve, než je navázáno cílové spojení
- Rozhodnutí řízené sítí na základě hlášení měření od UE
- Zahrnuje krátké, ale nevyhnutelné přerušení datového přenosu
- Standardní typ předávání pro GSM, LTE a 5G NR (ve scénářích bez duální konektivity)
- Vyžaduje přidělení rádiových prostředků v cílové buňce před provedením
- Používá explicitní zprávy Handover Command (příkaz k předání) a Handover Complete (předání dokončeno)

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.404** (Rel-19) — Performance Management Definitions & Template
- **TS 32.405** (Rel-19) — UTRAN Performance Measurements Specification
- **TS 32.863** (Rel-13) — PM Measurement Metadata Definition

---

📖 **Anglický originál a plná specifikace:** [HHO na 3GPP Explorer](https://3gpp-explorer.com/glossary/hho/)
