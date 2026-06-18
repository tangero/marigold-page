---
slug: "fss"
url: "/mobilnisite/slovnik/fss/"
type: "slovnik"
title: "FSS – Fixed Satellite Service"
date: 2025-01-01
abbr: "FSS"
fullName: "Fixed Satellite Service"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fss/"
summary: "FSS označuje satelitní komunikační služby, které zajišťují konektivitu mezi pevnými body na Zemi, jako jsou pozemní stanice a uživatelské terminály, za použití geostacionárních nebo negeostacionárních"
---

FSS je satelitní komunikační služba pro pevné pozemní stanice, která v rámci 3GPP umožňuje integraci satelitních sítí s 5G za účelem rozšíření pokrytí a vytvoření části nepozemských sítí (NTN).

## Popis

Pevná satelitní služba (Fixed Satellite Service, FSS) je telekomunikační služba definovaná Mezinárodní telekomunikační unií ([ITU](/mobilnisite/slovnik/itu/)) a začleněná do standardů 3GPP pro 5G nepozemské sítě ([NTN](/mobilnisite/slovnik/ntn/)). FSS využívá satelity k vytvoření komunikačních spojení mezi pevnými pozemními stanicemi, které mohou zahrnovat brány, rozbočovače a uživatelské terminály na stacionárních místech. V kontextu 3GPP je FSS integrována jako součást NTN, aby doplnila pozemní 5G sítě a poskytla konektivitu v oblastech, kde je pozemská infrastruktura nepraktická nebo nedostupná. Služba funguje na různých satelitních drahách, především na geostacionární dráze ([GEO](/mobilnisite/slovnik/geo/)) pro širokoplošné pokrytí a na negeostacionárních drahách ([NGSO](/mobilnisite/slovnik/ngso/)), jako je nízká oběžná dráha ([LEO](/mobilnisite/slovnik/leo/)), pro sníženou latenci. FSS podporuje jak transparentní (bent-pipe), tak regenerativní (on-board processing) architektury satelitních užitečných nákladů, které přenášejí signály mezi pozemními segmenty.

Z architektonického hlediska zahrnuje FSS v rámci 3GPP několik klíčových komponent: satelitní kosmický segment, který zahrnuje satelit s jeho transpondéry a anténami; pozemní segment, zahrnující pevné pozemní stanice (brány), které se připojují k páteřní síti; a uživatelské zařízení (UE) se satelitními terminály. Satelit funguje jako převodník, přijímá signály z pozemní stanice (uplink), zesiluje a převádí je a vysílá je zpět na jiný pevný bod (downlink). Při integraci s 5G NTN může satelit fungovat jako uzel rádiové přístupové sítě (RAN), například jako gNB, nebo jako transparentní opakovač. Pozemní stanice se připojuje k 5G páteřní síti (5GC) prostřednictvím standardních rozhraní (např. [N2](/mobilnisite/slovnik/n2/)/N3), což umožňuje plynulou kontinuitu služeb. Mezi klíčové technické aspekty patří zvládání dlouhých prodlev šíření (zejména u GEO), Dopplerových posunů (u NGSO) a velkých velikostí buněk způsobených satelitními pokrytími.

Při provozu FSS funguje tak, že vytváří komunikační cestu přes satelit. Například v 5G scénáři odešle pevný uživatelský terminál data přes satelit (uplink) na pozemní bránu; brána pak směruje provoz přes 5GC k cíli. Proces zahrnuje specifické adaptace definované v 3GPP, jako jsou úpravy časového předstihu pro kompenzaci zpoždění a modifikované procedury náhodného přístupu, které zohledňují pohyb satelitu. FSS může poskytovat různé služby: přenos (backhaul) pro pozemní základnové stanice, přímou konektivitu pro pevné uživatele a distribuci vysílání/vícebodového vysílání. Služba využívá kmitočtová pásma přidělená pro FSS organizací ITU, jako jsou pásma C, Ku a Ka, která nabízejí různé kompromisy mezi pokrytím, šířkou pásma a náchylností k vlivům počasí.

Úloha FSS v 5G spočívá v rozšíření pokrytí sítě a zvýšení spolehlivosti služeb. Integrací FSS do NTN umožňuje 3GPP globální konektivitu, včetně odlehlých venkovských oblastí, námořních a leteckých platforem. Podporuje 5G případy užití, jako je masivní IoT pro zemědělství nebo monitorování životního prostředí, kde je pozemské pokrytí řídké. FSS také poskytuje redundanci pro kritické komunikace, což zajišťuje odolnost sítě při výpadcích pozemských sítí (např. při přírodních katastrofách). Navíc umožňuje efektivní řešení pro přenos (backhaul) spojující izolované pozemní lokality s páteřní sítí, čímž snižuje náklady na infrastrukturu. Jako součást širšího rámce NTN pomáhá FSS naplnit vizi všudypřítomné 5G konektivity, překlenout digitální propast a podporovat nové aplikace vyžadující pokrytí všude.

## K čemu slouží

FSS byla začleněna do standardů 3GPP, aby řešila omezení pozemských sítí při poskytování univerzálního pokrytí, zejména v geograficky náročných nebo řídce osídlených regionech. Tradiční pozemní 5G sítě spoléhají na husté nasazení základnových stanic, což je ekonomicky neproveditelné v odlehlých oblastech, jako jsou pouště, oceány nebo hory. Historický kontext ukazuje, že satelitní komunikace tyto regiony dlouho obsluhovaly, ale dřívější standardy mobilních sítí (např. 2G-4G) plně neintegrovaly satelitní schopnosti, což vedlo k fragmentovaným řešením konektivity. Motivací pro FSS v 5G je potřeba dosáhnout plynulého globálního pokrytí, což je klíčový cíl vývoje 5G, a podpora nových případů užití, jako je autonomní lodní doprava, vzdálený průmyslový IoT a záchranné služby.

Vytvoření FSS v rámci 3GPP bylo hnací silou konvergence satelitních a pozemských technologií, umožněné pokrokem v satelitních konstelacích (např. mega-konstelacích [LEO](/mobilnisite/slovnik/leo/)) a standardizovaných rozhraních. Předchozí přístupy zacházely se satelitními sítěmi jako se samostatnými systémy, které vyžadovaly dvou režimová zařízení a složité roamingové dohody. Definováním FSS jako součásti [NTN](/mobilnisite/slovnik/ntn/) umožňuje 3GPP jednotnou správu sítě a kontinuitu služeb mezi pozemskými a satelitními segmenty. Tím se řeší problémy, jako jsou mezery v pokrytí, které brání adopci 5G pro kritické aplikace v dopravě, energetice a veřejné bezpečnosti. FSS navíc poskytuje řešení pro přenos (backhaul) v oblastech bez optické infrastruktury, čímž snižuje náklady a čas nasazení sítě.

Řešením těchto problémů FSS zvyšuje všestrannost a odolnost 5G sítí. Umožňuje operátorům nabízet konzistentní služby po celém světě a podporuje globální mobilitu uživatelů a zařízení. Integrace také otevírá nové obchodní modely, jako je satelitní 5G pro leteckou nebo námořní konektivitu. FSS dále přispívá k obnově po katastrofách tím, že poskytuje alternativní komunikační cesty při poškození pozemských sítí. Celkově FSS v 3GPP představuje strategické rozšíření 5G mimo pozemské hranice a zajišťuje, že výhody vysokorychlostní komunikace s nízkou latencí mohou dosáhnout každého koutu zeměkoule, čímž naplňuje příslib skutečně všudypřítomné konektivity.

## Klíčové vlastnosti

- Poskytuje pevnou konektivitu prostřednictvím satelitu pro integraci s 5G NTN
- Podporuje jak GEO, tak NGSO satelitní dráhy
- Umožňuje přenos (backhaul) a přímý přístup pro pevné uživatelské terminály
- Integruje se s 5GC prostřednictvím standardizovaných rozhraní (např. N2/N3)
- Zvládá dlouhé prodlevy šíření a Dopplerovy efekty
- Využívá kmitočtová pásma přidělená pro FSS organizací ITU (např. pásma C, Ku, Ka)

## Definující specifikace

- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.115** (Rel-19) — NR Repeater RF Conformance Testing Part 1
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.821** (Rel-16) — NR Support for Non-Terrestrial Networks
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec
- **TR 38.908** (Rel-19) — NR Band n104 FSS UL Protection

---

📖 **Anglický originál a plná specifikace:** [FSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/fss/)
