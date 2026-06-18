---
slug: "isb"
url: "/mobilnisite/slovnik/isb/"
type: "slovnik"
title: "ISB – Idle-State Biasing"
date: 2025-01-01
abbr: "ISB"
fullName: "Idle-State Biasing"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/isb/"
summary: "Idle-State Biasing (ISB) je mechanismus řízený sítí, který ovlivňuje chování uživatelského zařízení (UE) v idle módu při výběru a převýběru buňky (cell selection/reselection) aplikací bias offsetu ke"
---

ISB je mechanismus řízený sítí, který ovlivňuje výběr buňky (cell selection) u UE v idle módu aplikací offsetu, čímž navádí UE k preferovaným buňkám za účelem distribuce zátěže a optimalizace kapacity.

## Popis

Idle-State Biasing (ISB) je základní funkce v rámci protokolu 3GPP Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), konkrétně definovaná pro idle mód (RRC_IDLE) uživatelského zařízení (UE). Jejím hlavním účelem je modifikovat proces hodnocení buněk používaný UE pro výběr a převýběr buňky aplikací konfigurovatelného, buňce-specifického offsetu. Tento offset, hodnota Idle-State Biasing, je vysílán sítí jako část systémové informace ([SIB](/mobilnisite/slovnik/sib/)) buňky. Když UE vyhodnocuje kandidátní buňky, spočítá kritérium pro výběr buňky (např. S-kritérium v LTE, založené na [RSRP](/mobilnisite/slovnik/rsrp/)/[RSRQ](/mobilnisite/slovnik/rsrq/)) a následně k vypočtené hodnotě přičte hodnotu ISB přijatou od dané buňky. Tím je uměle zvýšena (nebo snížena) vnímaná kvalita této buňky, čímž je ovlivněno rozhodnutí UE.

Z architektonického hlediska je ISB parametr řízený rádiovou přístupovou sítí (RAN), konkrétně eNodeB v LTE nebo gNB v 5G NR. Jeho hodnota je stanovena nástroji pro plánování a optimalizaci sítě na základě strategií nasazení, jako je podpora přesunu zátěže na small cells (piko/femto buňky) nebo na specifická frekvenční pásma (např. z vytížené makrovrstvy na méně využívanou vrstvu vyšších frekvencí). Parametr ISB je vysílán v blocích systémové informace (SIB), jako jsou SIB3, SIB4 a SIB5 v LTE, které obsahují informace pro převýběr buňky pro scénáře intra-frekvenční, inter-frekvenční a inter-RAT.

Provozně ISB funguje ve spojení s dalšími parametry převýběru buňky, jako jsou hysterezní hodnoty, prahové hodnoty a priority. Poskytuje podrobnější a buňce-specifický mechanismus řízení než jednoduché absolutní priority. Například operátor může nastavit vysokou pozitivní hodnotu ISB na small cell, aby přilákal UE v jejím okolí, čímž efektivně rozšíří její pokrytí pro účely idle módu a zvýší pravděpodobnost, že se na ní UE usadí (camp). Jakmile je UE usazeno, při zahájení spojení tak učiní z této ovlivněné buňky, což usnadňuje vyrovnávání přenosové zátěže. To se liší od mobility v connected módu (handover), protože ISB cíleně působí na energeticky úsporný idle stav, kdy UE aktivně nepřenáší data, ale periodicky monitoruje paging a provádí hodnocení pro převýběr buňky.

Jeho role je klíčová pro nasazení HetNet (Heterogenní sítě) a řízení provozu. Řízením distribuce UE v idle módu pomáhá ISB předem umístit UE na optimální buňky ještě před jejich přechodem do connected módu. Tím se snižuje potřeba okamžitých handoverů po navázání spojení, minimalizuje se signalizační zátěž a zlepšuje se statistické rozložení přenosové zátěže napříč síťovými vrstvami. Jde o základní nástroj pro funkce samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)), jako je Vyrovnávání zátěže (Load Balancing) a Optimalizace robustnosti mobility (Mobility Robustness Optimization).

## K čemu slouží

Idle-State Biasing byl zaveden k řešení výzev efektivní distribuce provozu v stále složitějších nasazeních heterogenních sítí (HetNet). Před jeho zavedením byl výběr a převýběr buňky primárně založen na naměřené síle/kvalitě rádiového signálu (např. [RSRP](/mobilnisite/slovnik/rsrp/) v LTE) s omezenou možností řízení ze strany operátora prostřednictvím absolutních priorit pro různé frekvenční vrstvy nebo rádiové přístupové technologie ([RAT](/mobilnisite/slovnik/rat/)). Tento přístup byl nedostatečný pro jemněji odstupňované navádění v rámci stejné prioritní vrstvy, zejména pro správu zátěže mezi překrývajícími se makro buňkami a small cells (jako jsou femtobuňky nebo pikobuňky). Bez biasování by UE přirozeně vybírala nejsilnější signál makro buňky, což často vedlo k nevyužití nasazené kapacity small cells a přetížení makrovrstvy.

Vytvoření ISB bylo motivováno potřebou flexibilnějšího, buňce-specifického mechanismu řízení provozu působícího v idle stavu. Základní problém, který řeší, je suboptimální počáteční bod připojení pro UE. Pokud se UE usadí na přetížené makro buňce kvůli silnému signálu, její následný přechod do connected módu okamžitě zatíží tuto buňku. ISB umožňuje síti jemně ovlivnit rozhodnutí o usazení (camping), a povzbuzuje tak UE, aby se usadila na méně zatížených nebo kapacitně bohatších buňkách (např. small cells), i když je jejich čistý signál o něco slabší. Toto proaktivní vyrovnávání zátěže v idle módu je efektivnější než reaktivní handovery v connected módu, protože snižuje selhání navazování spojení na přetížených buňkách a rozkládá počáteční přístupovou zátěž.

Historicky poskytl ISB operátorům sítí klíčový nástroj k využití plných kapacitních benefitů vrstvených síťových architektur. Vyřešil omezení čistě měřením řízené mobility v idle módu a umožnil optimalizaci sítě řízenou politikami. To bylo zásadní pro úspěch LTE-Advanced a novějších technologií, kde se hustá nasazení small cells stala klíčovou strategií pro zvýšení síťové kapacity a pokrytí. ISB umožňuje síti navádět UE k nejvhodnější buňce od okamžiku jejich 'probuzení', čímž zlepšuje celkovou spektrální efektivitu a uživatelský komfort.

## Klíčové vlastnosti

- Buňce-specifický offset aplikovaný na kritéria pro výběr/převýběr buňky
- Vysílán v systémové informaci (např. SIB) pro UE v idle módu
- Umožňuje navádění provozu k preferovaným buňkám (např. small cells)
- Funguje nezávisle na parametrech handoveru v connected módu
- Podporuje vyrovnávání zátěže a optimalizaci HetNet
- Konfigurovatelný pro každou frekvenční vrstvu a pro každou buňku

## Související pojmy

- [SIB – System Information Block](/mobilnisite/slovnik/sib/)

## Definující specifikace

- **TS 23.810** (Rel-8) — IMS Service Interaction Management Study
- **TS 37.461** (Rel-19) — Iuant Interface Layer 1 Specification

---

📖 **Anglický originál a plná specifikace:** [ISB na 3GPP Explorer](https://3gpp-explorer.com/glossary/isb/)
