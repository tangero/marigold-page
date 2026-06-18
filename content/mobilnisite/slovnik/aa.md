---
slug: "aa"
url: "/mobilnisite/slovnik/aa/"
type: "slovnik"
title: "AA – Antenna Array"
date: 2025-01-01
abbr: "AA"
fullName: "Antenna Array"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aa/"
summary: "AA označuje složený vyzařovací diagram anténního pole měřený v dBi, který reprezentuje kombinovaný vyzařovací diagram více anténních prvků. Je základním prvkem pro beamforming a prostorové zpracování"
---

AA je složený vyzařovací diagram anténního pole, měřený v dBi, který představuje kombinovaný vyzařovací diagram více anténních prvků pro beamforming a prostorové zpracování v pokročilých MIMO systémech.

## Popis

Anténní pole (AA) ve standardech 3GPP je strukturované uspořádání více vyzařovacích prvků, jejichž jednotlivé vyzařovací diagramy se kombinují a vytvářejí složený vyzařovací diagram. Tento složený diagram, vyjádřený v dBi (decibelech izotropních), charakterizuje zisk a směrové vlastnosti pole vzhledem k ideálnímu izotropnímu zářiči. AA není pouze fyzickým seskupením, ale klíčovou funkční entitou v oblasti vysokofrekvenční ([RF](/mobilnisite/slovnik/rf/)) domény, kde jsou amplituda a fáze signálů přiváděných na každý prvek přesně řízeny za účelem tvarování celkového elektromagnetického pole. Toto řízení umožňuje pokročilé techniky prostorového zpracování signálu, které jsou ústřední pro moderní systémy bezdrátové komunikace.

Architektura AA zahrnuje několik klíčových komponent: jednotlivé anténní prvky (jako jsou dipóly nebo plošné antény), napájecí síť, která distribuuje signál, a fázové posouvače nebo jednotky digitálního beamformingu, které upravují parametry signálu na každém prvku. V typické základnové stanici (např. gNB v 5G NR nebo [eNB](/mobilnisite/slovnik/enb/) v LTE) je AA integrována do anténního systému, často jako součást Aktivního Anténního Systému ([AAS](/mobilnisite/slovnik/aas/)), kde jsou jednotky transceiverů úzce propojeny s vyzařovacími prvky. Složený diagram je odvozen výpočtem činitele pole, který kombinuje činitel prvku (vyzařovací diagram jednotlivého prvku) s činitelem pole (efekt uspořádání prvků a jejich buzení). Výsledkem je směrový svazek, který lze elektronicky natáčet ke sledování uživatelského zařízení (UE), čímž se zvyšuje síla signálu a snižuje interference.

Princip fungování AA spočívá v principu superpozice a koherentního skládání signálů. Aplikací specifických komplexních vah (úprav amplitudy a fáze) na signály na každém prvku může pole konstruktivně interferovat v požadovaných směrech a destruktivně interferovat v jiných. Tento proces, známý jako beamforming, umožňuje AA soustředit energii směrem k cílovým UE a vytvářet tak svazky s vysokým ziskem. Ve scénářích multi-uživatelského [MIMO](/mobilnisite/slovnik/mimo/) ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)) lze současně generovat více svazků pro obsluhu různých UE, což využívá prostorového multiplexování ke zvýšení kapacity sítě. Složený diagram v dBi kvantifikuje tuto schopnost zaostřování a udává, jaký zisk pole poskytuje oproti izotropnímu zářiči v daném směru.

Role AA v síti je klíčová pro dosažení výkonnostních cílů 5G a dalších generací, jako je vylepšené mobilní širokopásmové připojení (eMBB), hromadná komunikace strojového typu (mMTC) a ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)). Tvoří základ klíčových technologií, jako je massive MIMO, kde se používají pole s desítkami nebo stovkami prvků k vytváření úzkých, adaptivních svazků. To zlepšuje pokrytí, zejména na vyšších frekvencích, jako je mmWave, kde je útlum na trase výrazný. Dále je vyzařovací diagram AA nezbytný pro zkušební shodu a ověřování výkonu, jak je specifikováno v dokumentech 3GPP pro zkoušky shody (např. TR 37.840, TR 38.817), což zajišťuje, že základnové stanice splňují požadavky na vyzařovací diagram pro reálné nasazení.

## K čemu slouží

Technologie anténního pole existuje proto, aby překonala omezení tradičních jedno-prvkových antén, které nabízejí pevné, všesměrové vyzařovací diagramy s omezeným ziskem a prostorovou kontrolou. Jak se mobilní sítě vyvíjely od 2G k 5G, poptávka po vyšších přenosových rychlostech, lepší spektrální účinnosti a zvýšené síťové kapacitě rostla exponenciálně. Jednotlivé antény nemohly podporovat pokročilé techniky jako beamforming nebo prostorové multiplexování, které jsou nezbytné pro splnění těchto požadavků. AA byla zavedena, aby poskytla flexibilní, elektronicky říditelný vyzařovací diagram, který se dokáže přizpůsobit dynamickým síťovým podmínkám, rozmístění uživatelů a zatížení provozem.

Historicky se rané mobilní systémy spoléhaly na pasivní antény se širokými pokryvovými diagramy, což vedlo k neefektivitám jako vysoká interference a omezená kapacita. Motivace pro vytvoření AA vycházela z potřeby využít prostorový rozměr rádiového kanálu. Použitím více anténních prvků mohou sítě přesně směrovat signály, čímž snižují plýtvání energií a zmírňují interference. To je obzvláště kritické v hustých městských prostředích a pro vyšší kmitočtová pásma (např. mmWave v 5G), kde jsou výzvou útlum signálu a překážky. AA to řeší tím, že umožňuje vytváření zaostřených svazků, které prodlužují dosah a zlepšují spolehlivost.

Omezení předchozích přístupů zahrnovala statické vyzařovací diagramy, které se nedokázaly přizpůsobit pohybujícím se uživatelům nebo měnícímu se prostředí, což vedlo k špatnému výkonu pro mobilní širokopásmo a nově vznikající IoT aplikace. Technologie AA to řeší tím, že umožňuje dynamické natáčení a tvarování svazků, což zlepšuje uživatelský zážitek prostřednictvím vyšší propustnosti a nižší latence. Také podporuje cíle zhušťování sítě a energetické účinnosti, protože svazky mohou být aktivovány pouze tam, kde jsou potřeba, čímž se snižuje celková spotřeba energie. Měření složeného diagramu v dBi standardizuje hodnocení výkonu a zajišťuje interoperabilitu a konzistentní nasazení napříč výrobci a operátory.

## Klíčové vlastnosti

- Složený vyzařovací diagram vyjádřený v dBi pro standardizované měření zisku
- Umožňuje elektronický beamforming a natáčení svazku pro směrový přenos signálu
- Podporuje konfigurace massive MIMO s desítkami až stovkami anténních prvků
- Umožňuje prostorové multiplexování pro multi-uživatelské MIMO ke zvýšení síťové kapacity
- Integruje se s Aktivními Anténními Systémy (AAS) pro integrovanou funkci transceiveru
- Nezbytný pro provoz na mmWave kmitočtech k potlačení vysokého útlumu na trase prostřednictvím zaostřování svazku

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 33.804** (Rel-12) — Non-UICC SSO using SIP Digest credentials
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 37.840** (Rel-12) — RF & EMC Requirements for Active Antenna Systems
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [AA na 3GPP Explorer](https://3gpp-explorer.com/glossary/aa/)
