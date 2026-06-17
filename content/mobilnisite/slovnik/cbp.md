---
slug: "cbp"
url: "/mobilnisite/slovnik/cbp/"
type: "slovnik"
title: "CBP – Constrained Baseline Profile"
date: 2025-01-01
abbr: "CBP"
fullName: "Constrained Baseline Profile"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cbp/"
summary: "Standardizovaný profil v rámci služby Multimedia Telephony Service for IMS (MTSI) konsorcia 3GPP, který definuje minimální povinnou sadu kodeků a funkcí. Zajišťuje základní interoperabilitu hlasových"
---

CBP (Constrained Baseline Profile) je minimální profil standardu 3GPP MTSI, který zajišťuje základní interoperabilitu hlasových a videohovorů pro zařízení s omezenými zdroji a nízkonákladové síťové implementace.

## Popis

Profil Constrained Baseline Profile (CBP) je formální specifikace v rámci architektury služby Multimedia Telephony Service for IMS ([MTSI](/mobilnisite/slovnik/mtsi/)) konsorcia 3GPP, definovaná napříč několika technickými specifikacemi (TS). Jeho hlavní funkcí je vytvoření garantovaného základu pro multimediální komunikační schopnosti. Toho dosahuje tím, že stanovuje minimální, nevyjednatelnou sadu audio a video kodeků, kterou musí podporovat každý koncový bod vyhovující CBP. Tento profil se odlišuje od Primárního profilu (PP), který nabízí bohatší sadu schopností pro pokročilá zařízení. Architektura CBP je definována v kontextu vyjednávání relace, kdy si koncové body prostřednictvím SIP/SDP (Session Initiation Protocol/Session Description Protocol) vyměňují informace o podporovaných profilech a kodecích. Když koncový bod deklaruje podporu CBP, zavazuje se podporovat povinné kodeky, čímž zajišťuje, že lze navázat základní multimediální relaci, i když mají zařízení výrazně odlišné schopnosti nebo jsou od různých výrobců.

Operačně CBP funguje tak, že omezuje prostor pro vyjednávání kodeků. Pro audio je povinným kodekem typicky varianta s nízkou složitostí, jako je [AMR](/mobilnisite/slovnik/amr/) (Adaptive Multi-Rate) nebo [AMR-WB](/mobilnisite/slovnik/amr-wb/) (Wideband), vybraná pro svou širokou podporu a efektivní výkon na procesorech s nízkým příkonem. Pro video profil ukládá povinnost podporovat omezenou verzi H.264/[AVC](/mobilnisite/slovnik/avc/), často se specifickými omezeními profilů, úrovní (level) a datových toků, aby se snížily nároky na výpočetní výkon a paměť. Role sítě, primárně prostřednictvím IMS core a funkce Policy and Charging Rules Function (PCRF), spočívá v usnadňování relací a aplikování příslušných QoS politik, ale samotný CBP je schopností koncového bodu. Klíčovými komponentami jsou uživatelské zařízení (UE) implementující CBP, IMS core zpracovávající signalizaci relace a přenosová rovina (media plane), kde se používají stanovené kodeky pro paketizaci a přenos.

Jeho role v síti je zásadně o zajištění interoperability a umožnění trhu. Tím, že poskytuje formalizovaný 'nejnižší společný jmenovatel', umožňuje výrobcům s důvěrou vyrábět extrémně cenově optimalizovaná zařízení pro specifické tržní segmenty (např. nízkorozpočtové smartphony, IoT zařízení s komunikačními funkcemi) s jistotou, že budou schopna vzájemné spolupráce pro základní služby. Také zjednodušuje testování a certifikaci, protože sada funkcí je jasně vymezena. CBP je klíčový pro naplnění vize 3GPP o všudypřítomné multimediální telefonii, zajišťuje, že pokrytí službami a jejich kvalita nebudou výsadou pouze špičkových zařízení, a tím podporuje širší adopci a konzistentní uživatelský zážitek napříč ekonomickými a technologickými rozdíly.

## K čemu slouží

CBP byl vytvořen, aby vyřešil kritickou mezeru na trhu a technickou překážku ve vývoji telefonních služeb založených na IMS. Když 3GPP vyvíjelo bohaté multimediální služby ([MTSI](/mobilnisite/slovnik/mtsi/)) v releasích jako Rel-9 a Rel-10, definované schopnosti a sady kodeků (např. v Primárním profilu) byly navrženy pro výkonné smartphony. To vytvořilo bariéru vstupu pro segment nízkonákladových zařízení, protože implementace celé, komplexní sady volitelných kodeků a funkcí byla ekonomicky a technicky neúnosná. Bez standardizovaného 'nízkorozpočtového' profilu nebylo možné garantovat interoperabilitu základních hlasových a videohovorů mezi nízkonákladovými a špičkovými zařízeními, což mohlo fragmentovat trh a bránit rozsáhlému nasazení IMS služeb.

Hlavním problémem, který řeší, je zajištění garantované základní interoperability. Před CBP mohly koncové body podporovat různé podmnožiny desítek volitelných kodeků. Navázání relace mohlo selhat, pokud se nenašel společný kodek, nebo mohlo dojít k použití možnosti velmi nízké kvality. CBP stanovuje konkrétní, minimální sadu, čímž tuto nejistotu odstraňuje. Také řeší problém implementačních nákladů a složitosti pro výrobce zařízení cílené na cenově citlivé trhy. Definováním omezené sady funkcí snižuje potřebný výpočetní výkon, paměť a licenční náklady spojené s podporou více pokročilých kodeků, jako jsou vysokovýkonné video kodeky ([HEVC](/mobilnisite/slovnik/hevc/)).

Historicky bylo jeho zavedení v Rel-12 motivováno snahou průmyslu rozšířit služby Voice over LTE (VoLTE) a Video over LTE (ViLTE) založené na IMS mimo prémiová zařízení na masový trh. Umožnilo vytvoření víceúrovňového ekosystému služeb: špičková zařízení používají Primární profil pro vyšší kvalitu a zařízení s omezenými náklady používají CBP pro spolehlivé základní služby. To bylo zásadní pro operátory usilující o migraci všech uživatelů na služby založené na IP a vyřazení starých přepojovaných sítí, neboť poskytovalo proveditelnou cestu pro segmenty zákazníků s nízkým [ARPU](/mobilnisite/slovnik/arpu/) (Average Revenue Per User).

## Klíčové vlastnosti

- Stanovuje povinnou podporu minimální sady audio kodeků (např. AMR, AMR-WB) pro garantovanou hlasovou interoperabilitu
- Stanovuje povinnou podporu omezené základní verze video kodeku H.264/AVC s definovanými limity profilu a úrovně (level)
- Definuje formální 3GPP profil v rámci specifikací MTSI, což zajišťuje standardizaci napříč dodavateli
- Umožňuje spolehlivé navázání relace mezi zařízeními s výrazně odlišnými schopnostmi tím, že poskytuje společný jmenovatel
- Snižuje složitost implementace a náklady pro uživatelská zařízení (UE) cílená na segmenty s omezenými zdroji nebo nízkými náklady
- Spolupracuje s vyjednáváním IMS relace (SIP/SDP) při deklaraci podpory profilu a výběru povinných kodeků

## Související pojmy

- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TR 26.923** (Rel-19) — Study on IMS-based Telepresence Media Handling
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CBP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbp/)
