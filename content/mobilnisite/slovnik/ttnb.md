---
slug: "ttnb"
url: "/mobilnisite/slovnik/ttnb/"
type: "slovnik"
title: "TTNB – Time to Next Burst"
date: 2025-01-01
abbr: "TTNB"
fullName: "Time to Next Burst"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ttnb/"
summary: "Time to Next Burst (TTNB) je parametr používaný v architektuře Integrated Access and Backhaul (IAB) podle 3GPP, konkrétně pro provoz ve sdíleném nebo nelicencovaném spektru. Udává časový interval, po"
---

TTNB je časový interval, po který musí uzel IAB čekat, než zahájí přenosový dávkový přenos na sdíleném kanálu po provedení procedury poslechu před vysíláním (Listen-Before-Talk).

## Popis

Time to Next Burst (TTNB) je klíčový časovací parametr na vrstvě řízení přístupu k médiu (Medium Access Control, [MAC](/mobilnisite/slovnik/mac/)) uzlu Integrated Access and Backhaul ([IAB](/mobilnisite/slovnik/iab/)) provozovaného ve sdíleném spektru, jako je 5G NR-Unlicensed ([NR-U](/mobilnisite/slovnik/nr-u/)). Jeho hlavní funkcí je spravovat přístup ke kanálu spravedlivým a regulačním požadavkům vyhovujícím způsobem vedle jiných technologií rádiového přístupu ([RAT](/mobilnisite/slovnik/rat/)), jako je Wi-Fi ([IEEE](/mobilnisite/slovnik/ieee/) 802.11). TTNB je určen a signalizován jako součást procedury přístupu ke kanálu, konkrétně po úspěšné kontrole poslechu před vysíláním (Listen-Before-Talk, [LBT](/mobilnisite/slovnik/lbt/)). Když uzel IAB získá přístup ke kanálu, je mu obvykle přidělena přenosová příležitost (Transmission Opportunity, TXOP) – ohraničené časové okno, během kterého může vysílat dávku datových rámců. TTNB je časový interval od konce aktuální TXOP (nebo dávky) do očekávaného času zahájení další přenosové dávky uzlu.

Z architektonického hlediska je TTNB vypočítáván a využíván distribuovanou jednotkou uzlu IAB ([IAB-DU](/mobilnisite/slovnik/iab-du/)). Proces funguje následovně: Před vysíláním provede IAB-DU proceduru LBT (např. LBT kategorie 4, podobnou [CSMA/CA](/mobilnisite/slovnik/csma-ca/) u Wi-Fi), aby se ujistil, že kanál je volný. Po úspěšném přístupu vysílá svou dávku dat. Stanovení TTNB může být založeno na několika faktorech, včetně vlastní nevyřízené přenosové zátěže uzlu, požadavků na kvalitu služeb (Quality of Service, QoS) obsluhovaných uživatelských zařízení (UE) a podřízených uzlů IAB, a potenciálně centralizovaných návrhů plánování od IAB donoru. Tato hodnota TTNB může být implicitně odvozena z plánovacího algoritmu uzlu nebo explicitně signalizována jiným entitám. V některých koordinačních schématech může uzel IAB oznámit svůj TTNB sousedním uzlům (přímou signalizací nebo prostřednictvím donoru), aby usnadnil prostorovou reutilizaci a minimalizoval problém skrytého uzlu.

Klíčovými komponentami, které se podílejí, jsou plánovač MAC a entita LBT v IAB-DU. TTNB přímo ovlivňuje vzor přístupu ke kanálu a latenci pro provoz procházející uzlem IAB. Krátký TTNB znamená, že uzel má v úmyslu znovu brzy přistoupit ke kanálu, což je vhodné pro provoz citlivý na latenci nebo s vysokou prioritou. Dlouhý TTNB uvolňuje kanál pro jiné uzly nebo RAT, což podporuje spravedlnost. Tento parametr je zásadní pro dosažení dvojího cíle efektivního provozu NR-U: maximalizace propustnosti systému NR při zajištění spravedlivé koexistence se stávajícími systémy, jak vyžadují předpisy (např. ETSI EN 301 893 pro pásmo 5 GHz).

## K čemu slouží

TTNB byl zaveden, aby řešil specifické výzvy nasazení 5G NR v nelicencovaných nebo sdílených kmitočtových pásmech, zejména v kontextu IAB. Tradiční provoz v licencovaném spektru používá těsně synchronizovaný, naplánovaný přístup řízený výhradně stanicí gNB, který nevyžaduje mechanismy jako TTNB. Nicméně nelicencované spektrum vyžaduje přístup založený na soutěžení (např. LBT), aby byla zajištěna spravedlivá koexistence s jinými technologiemi, jako je Wi-Fi. Problém je, že bez koordinace by mohlo více uzlů IAB patřících do stejné sítě soutěžit mezi sebou i proti Wi-Fi, což vede k neefektivnímu využití kanálu a zvýšenému počtu kolizí.

Vytvoření TTNB je motivováno potřebou přinést určitou míru předvídatelnosti a koordinace do inherentně náhodného přístupu ke kanálu založeného na LBT v rámci řízené sítě IAB. Řeší omezení čistě distribuovaného, nezávislého LBT, které může vést k suboptimálnímu výkonu systému NR jako celku. Tím, že má pojem 'čas do další dávky', může uzel IAB plánovat své pokusy o přístup ke kanálu a tuto informaci mohou použít nadřazené uzly nebo donory k provádění inteligentní alokace zdrojů a správy interference v topologii IAB. To je zvláště důležité pro backhaulové spoje, které přenášejí agregovaný provoz a mají přísnější požadavky na latenci a spolehlivost než typické přístupové spoje.

Historicky tento koncept navazuje na mechanismy koexistence vyvinuté pro LTE-Licensed Assisted Access (LAA) v Rel-13/14, které zavedly LBT a TXOP. TTNB v IAB pro NR-U v Rel-19 rozšiřuje tyto myšlenky do kontextu více-skokové, meshové sítě. Řeší dodatečnou složitost zajištění toho, aby přístup ke kanálu na backhaulovém spoji nevyhladověl přístupový spoj stejného uzlu nebo nezpůsobil nadměrnou latenci pro skoky hluboko v síti IAB. TTNB je tedy klíčovým prvkem umožňujícím efektivní, vysoce výkonné a spravedlivé bezdrátové vlastní backhaulování ve sdíleném spektru, což je zásadní pro rychlé a nákladově efektivní zhušťování sítě.

## Klíčové vlastnosti

- Časovací parametr používaný uzly IAB pro koordinaci přístupu ke kanálu ve sdíleném/nelicencovaném spektru (např. NR-U)
- Definuje očekávanou dobu čekání od konce aktuální přenosové dávky do začátku další dávky pro stejný uzel
- Usnadňuje spravedlivou koexistenci s jinými technologiemi rádiového přístupu (jako je Wi-Fi) a mezi samotnými uzly IAB
- Je určen po úspěšné proceduře poslechu před vysíláním (Listen-Before-Talk, LBT) a může být založen na přenosové zátěži a požadavcích QoS
- Umožňuje předvídatelnější a efektivnější plánování v rámci sítě IAB, čímž zlepšuje latenci a propustnost backhaulových spojů
- Lze použít pro implicitní nebo explicitní koordinaci mezi sousedními přenosovými body k optimalizaci prostorové reutilizace

## Definující specifikace

- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 38.415** (Rel-19) — PDU Session User Plane Protocol
- **TS 38.425** (Rel-19) — NR User Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [TTNB na 3GPP Explorer](https://3gpp-explorer.com/glossary/ttnb/)
