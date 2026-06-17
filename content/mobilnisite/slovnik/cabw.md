---
slug: "cabw"
url: "/mobilnisite/slovnik/cabw/"
type: "slovnik"
title: "CABW – Cumulative Aggregated Channel Bandwidth"
date: 2025-01-01
abbr: "CABW"
fullName: "Cumulative Aggregated Channel Bandwidth"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/cabw/"
summary: "CABW je klíčový parametr v 5G NR definující celkovou agregovanou šířku pásma, kterou může UE podporovat napříč všemi svými aktivními komponentními nosnými. Jde o zásadní schopnost UE určující dosažite"
---

CABW je celková agregovaná šířka pásma, kterou může uživatelské zařízení (UE) podporovat napříč všemi svými aktivními komponentními nosnými v 5G NR. Jde o klíčovou schopnost, která určuje maximální datové rychlosti a ovlivňuje konfiguraci agregace nosných.

## Popis

CABW (Cumulative Aggregated Channel Bandwidth, kumulativní agregovaná šířka pásma kanálu) je zásadní parametr schopností UE definovaný ve specifikacích 3GPP NR, konkrétně v TS 38.101. Představuje maximální celkovou šířku pásma, měřenou v MHz, kterou je uživatelské zařízení (UE) schopno současně podporovat napříč všemi svými agregovanými komponentními nosnými ([CC](/mobilnisite/slovnik/cc/)) v dané kombinaci kmitočtových pásem. Nejde pouze o součet šířek pásem jednotlivých nosných, ale o definovanou horní mez, která omezuje celkovou šířku pásma pro přenos a příjem, kterou řetězce vysokofrekvenčního (RF) a základního pásma UE dokážou současně zpracovat. Hodnotu CABW hlásí UE síti během procedur výměny informací o schopnostech, typicky jako součást informačních elementů UE-NR-Capability nebo UE-MRDC-Capability.

Koncept CABW je neodmyslitelně spojen s agregací nosných ([CA](/mobilnisite/slovnik/ca/)) a v pozdějších verzích s duální konektivitou ([DC](/mobilnisite/slovnik/dc/)) a multi-radio duální konektivitou ([MR-DC](/mobilnisite/slovnik/mr-dc/)). Když síť nakonfiguruje UE s více komponentními nosnými – ať už jde o vnitropásmově souvislé, vnitropásmově nesouvislé nebo mezipásmové – kombinovaná šířka pásma kanálu této konfigurace nesmí překročit UE nahlášené CABW pro tuto konkrétní kombinaci pásem. Vrstva řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) sítě tyto informace používá k inteligentnímu plánování a rozhodování o správě nosných. Například, pokud UE nahlásí CABW 200 MHz pro určitou kombinaci pásem, gNB může agregovat nosné až do tohoto celkového limitu, ale musí se vyvarovat konfigurací, které by jej překročily, neboť by to přesáhlo možnosti zpracování fyzické vrstvy UE.

Z architektonického hlediska je CABW omezení, které ovlivňuje jak návrh vysokofrekvenčního koncového stupně (front-endu) UE, tak jeho jednotku základního pásma. Vysokofrekvenční koncový stupeň, včetně filtrů, zesilovačů a směšovačů, musí být navržen tak, aby zvládal signály v celé agregované šířce pásma bez nadměrného zkreslení nebo šumu. Současně musí být zpracování základního pásma, zahrnující operace rychlé Fourierovy transformace ([FFT](/mobilnisite/slovnik/fft/)) / inverzní FFT ([IFFT](/mobilnisite/slovnik/ifft/)), odhad kanálu a ekvalizaci, dimenzováno tak, aby zpracovalo odpovídající počet zdrojových bloků v celé CABW. Parametr je definován pro každou podporovanou kombinaci pásem (např. Pásmo n78 + Pásmo n78, nebo Pásmo n41 + Pásmo n71), protože vysokofrekvenční složitost a požadované ochranné intervaly se mezi kombinacemi liší, což ovlivňuje celkovou únosnou agregovanou šířku pásma.

Jeho role v síti je klíčová pro optimalizaci výkonu a správu rušení. Díky znalosti CABW může gNB přizpůsobit konfiguraci agregace nosných tak, aby maximalizoval propustnost UE při zajištění spolehlivého provozu. Zabrání síti přiřadit konfiguraci prostředků, kterou UE není fyzicky schopna podporovat, což by vedlo k selhání rádiového spoje nebo zhoršení výkonu. CABW je navíc klíčovým faktorem pro síťové segmenty (network slicing) a poskytování kvality služeb (QoS) pro služby rozšířeného mobilního broadbandu (eMBB), neboť přímo omezuje špičkovou datovou rychlost dostupnou pro segment nebo QoS Flow pro dané UE. CABW je tedy úhelným parametrem, který propojuje hardwarové schopnosti UE se správou síťových prostředků, umožňuje efektivní využití fragmentovaného spektra a podporuje vysoké datové rychlosti slibované 5G NR.

## K čemu slouží

Hlavním účelem definice CABW je poskytnout standardizovaný a jednoznačný způsob, jak může UE komunikovat své hardwarové limity týkající se celkového zpracovávaného pásma síti. Tím se řeší kritický problém, kdy by síť mohla nakonfigurovat nastavení agregace nosných překračující fyzické možnosti UE z hlediska vysokofrekvenčního příjmu/vysílání a výkonu zpracování základního pásma. Bez tohoto parametru by musela síť činit předpoklady nebo používat metodu pokusu a omylu, což by vedlo k potenciálním selháním rádiového spoje, zvýšené signalizační režii a suboptimálnímu uživatelskému zážitku.

Historicky, jak se buněčné sítě vyvíjely ze 4G LTE na 5G NR, se používání agregace nosných stalo složitějším a rozšířenějším. 5G zavedlo podporu širších šířek pásma komponentních nosných (až 100 MHz na nosnou v FR1 a 400 MHz v FR2) a různorodějších kombinací pásem včetně milimetrových vln (mmWave). To zvýšilo potenciální celkovou agregovanou šířku pásma daleko za to, co bylo typické v LTE. Různé kategorie a formy faktorů UE (např. smartphony, IoT moduly, [CPE](/mobilnisite/slovnik/cpe/)) mají výrazně odlišné hardwarové schopnosti a cenové cíle. Výkonný smartphone může podporovat velkou CABW pro špičkový výkon, zatímco senzor IoT s nízkou spotřebou může podporovat velmi malou CABW. Parametr CABW umožňuje tuto diferenciaci standardizovaným způsobem.

Zavedení CABW bylo motivováno potřebou efektivního a spolehlivého řízení rádiových prostředků v tomto novém, komplexnějším prostředí. Řeší omezení předchozích přístupů, kdy byly schopnosti šířky pásma často definovány implicitně na komponentní nosnou nebo pásmo bez jasného celkového agregovaného limitu. Explicitním definováním CABW pro každou kombinaci pásem umožnila 3GPP inteligentnější síťové plánování, lepší správu výkonu UE (protože zpracování širšího pásma spotřebovává více energie) a flexibilnější návrh UE. Operátorům sítí umožňuje plně využít svá spektrální aktiva agregací nosných až do limitu, který každé UE zvládne, čímž maximalizují kapacitu sítě a uživatelskou propustnost bez kompromisů na stabilitě spojení.

## Klíčové vlastnosti

- Definuje maximální celkovou šířku pásma, kterou může UE podporovat napříč všemi agregovanými komponentními nosnými.
- Hlášeno jako parametr schopností UE pro každou podporovanou kombinaci kmitočtových pásem.
- Kritické pro rozhodování sítě při konfiguraci agregace nosných (CA) a duální konektivity (DC).
- Zajišťuje, že nakonfigurovaná šířka pásma nepřekročí vysokofrekvenční a základnovědové (baseband) limity UE.
- Přímo ovlivňuje maximální dosažitelnou špičkovou datovou rychlost pro UE.
- Umožňuje diferenciaci mezi kategoriemi UE (např. prémiová vs. nízkorozpočtová zařízení).

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions

---

📖 **Anglický originál a plná specifikace:** [CABW na 3GPP Explorer](https://3gpp-explorer.com/glossary/cabw/)
