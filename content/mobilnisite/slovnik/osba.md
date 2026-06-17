---
slug: "osba"
url: "/mobilnisite/slovnik/osba/"
type: "slovnik"
title: "OSBA – Objects (ISM) with Scene-Based Audio"
date: 2025-01-01
abbr: "OSBA"
fullName: "Objects (ISM) with Scene-Based Audio"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/osba/"
summary: "Objects (ISM) with Scene-Based Audio (OSBA) je standard 3GPP pro doručování imerzivního audio obsahu. Definuje, jak reprezentovat a streamovat zvukové scény složené z jednotlivých zvukových objektů a"
---

OSBA je standard 3GPP pro imerzivní audio, který definuje reprezentaci a streamování zvukových scén složených z jednotlivých zvukových objektů a metadat, což umožňuje personalizovaný, interaktivní prostorový zvuk.

## Popis

Objects ([ISM](/mobilnisite/slovnik/ism/)) with Scene-Based Audio (OSBA) je standard pro doručování médií v rámci architektury 3GPP Immersive Sound Model (ISM), speciálně navržený pro reprezentaci a vykreslování složitých, objektově založených zvukových scén. Zvuková scéna v OSBA není jediná monolitická audio stopa, ale kompozice více jednotlivých audio objektů, z nichž každý má svou vlastní audio esenci (zvuková data) a bohatá prostorová metadata. Tato metadata přesně definují pozici, pohyb, velikost a další akustické vlastnosti každého objektu v trojrozměrném souřadnicovém systému. Jádrem fungování OSBA je tvorba, zapouzdření, doručování a vykreslování těchto scén na straně klienta. Tvůrci obsahu vytvářejí scény pomocí nástrojů, které produkují audio objekty a metadata; ty jsou následně zabaleny podle specifikací 3GPP, typicky v kontejnerech [ISOBMFF](/mobilnisite/slovnik/isobmff/) ([MP4](/mobilnisite/slovnik/mp4/)) pro streamování.

Pro doručování OSBA využívá existující adaptivní streamovací protokoly jako [DASH](/mobilnisite/slovnik/dash/) nebo [HLS](/mobilnisite/slovnik/hls/). Audio objekty a jejich dynamická metadata jsou zabaleny jako samostatné mediální komponenty nebo stopy v rámci mediální prezentace. To umožňuje streamovacímu klientovi vyžádat a přijímat pouze komponenty nezbytné pro aktuální scénu a perspektivu uživatele. Klíčovým technickým aspektem je synchronizace audio esence objektu s jeho časově proměnnými prostorovými metadaty, což zajišťuje, že zvuky jsou vykresleny na správném místě ve správný čas. Renderer na straně klienta, který může být v chytrém telefonu, XR headsetu nebo domácím kině, přijímá tyto komponenty, dekóduje audio objekty a používá metadata k prostorovému vykreslení zvukové scény v reálném čase, často s využitím binauračního renderování pro sluchátka nebo kanálového renderování pro reproduktorové soustavy.

Role OSBA v síti je standardem mediálního formátu na aplikační vrstvě. Leží nad přenosovými schopnostmi jádra sítě a umožňuje poskytovatelům služeb nabízet audio zážitky nové generace. Je nedílnou součástí mediálních služeb, jako je rozšířená realita (XR), interaktivní živé události a personalizované audio pro video. Oddělením popisu zvukové scény (metadat) od audio esence OSBA umožňuje pokročilé funkce, jako je selektivní vylepšení objektů, funkce přístupnosti (např. zesílení komentářového audia) a efektivita šířky pásma, protože objekty lze přidávat, odebírat nebo nahrazovat na základě síťových podmínek nebo uživatelských preferencí bez nutnosti překódování celé scény.

## K čemu slouží

OSBA byla vytvořena, aby řešila omezení tradičních kanálově založených (např. 5.1, 7.1) a scénově založených (např. Ambisonics) audio formátů při poskytování skutečně imerzivních a interaktivních audio zážitků pro nově vznikající média. Kanálové audio je vázáno na konkrétní rozmístění reproduktorů a nenabízí žádnou interaktivitu, zatímco Ambisonics prvního řádu má omezené prostorové rozlišení. Vzestup aplikací, jako je virtuální realita (VR), rozšířená realita ([AR](/mobilnisite/slovnik/ar/)) a interaktivní 360stupňové video, vyžadoval audio formát schopný poskytnout přesný, dynamický prostorový zvuk, který reaguje na pohyby hlavy a interakce uživatele.

Primární problém, který OSBA řeší, je, jak efektivně streamovat složité, vícedobjektové zvukové scény přes potenciálně omezené mobilní sítě, a zároveň umožnit personalizaci a adaptaci na straně klienta. Předchozí přístupy buď vyžadovaly předmíchání audia pro konkrétní výstup (se ztrátou flexibility), nebo přenášely pole Ambisonics vyššího řádu (což může být neefektivní z hlediska šířky pásma a postrádá kontrolu na úrovni objektů). Objektově založený přístup OSBA umožňuje síti přenášet popis scény a diskrétní audio elementy, což umožňuje zařízení koncového uživatele provést finální, personalizované vykreslení. To je klíčové pro XR, kde se audio musí aktualizovat v reálném čase na základě orientace hlavy uživatele.

Motivací pro OSBA tedy bylo standardizovat interoperabilní formát pro objektově založené imerzivní audio, který zajišťuje, že obsah vytvořený jedním poskytovatelem může být správně vykreslen na zařízeních od různých výrobců. Tato standardizace, která je součástí širší práce 3GPP na mediálních kodecích a doručování, má za cíl katalyzovat ekosystém pro imerzivní mediální služby přes 5G a dále, a učinit tak personalizované audio kinematické kvality životaschopnou službou pro mobilní uživatele.

## Klíčové vlastnosti

- Objektově založená reprezentace audio scény s jednotlivými audio objekty a metadaty
- Přesná 3D prostorová metadata definující pozici, šířku a pohyb objektu
- Synchronizované doručování audio esence a dynamických streamů prostorových metadat
- Podpora personalizovaného vykreslování na straně klienta na základě uživatelské perspektivy (např. sledování polohy hlavy)
- Efektivní zabalení a streamování s využitím protokolů ISOBMFF a DASH/HLS
- Umožňuje interaktivní audio funkce, jako je výběr objektů, jejich zvýraznění a úpravy pro přístupnost

## Související pojmy

- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals

---

📖 **Anglický originál a plná specifikace:** [OSBA na 3GPP Explorer](https://3gpp-explorer.com/glossary/osba/)
