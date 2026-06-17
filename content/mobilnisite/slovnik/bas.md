---
slug: "bas"
url: "/mobilnisite/slovnik/bas/"
type: "slovnik"
title: "BAS – Broadcast Auxiliary Service"
date: 2025-01-01
abbr: "BAS"
fullName: "Broadcast Auxiliary Service"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bas/"
summary: "Služba umožňující poskytovatelům vysílacího obsahu využívat sítě 5G pro přenosové a příspěvkové spoje. Poskytuje spolehlivý, kvalitní přenos živých audio/video přenosů z odlehlých míst do vysílacích s"
---

BAS je služba 3GPP, která umožňuje vysílacím organizacím využívat sítě 5G jako spolehlivý a kvalitní přenosový prostředek pro živé audio/video přenosy z odlehlých míst do jejich studií.

## Popis

Broadcast Auxiliary Service (BAS) je specializovaná služba definovaná ve standardech 3GPP, která využívá sítě 5G pro podporu profesionálních vysílacích operací. Funguje jako řízená přenosová služba pro příspěvkové a distribuční spoje vysílání, přenášející vysoce kvalitní audio a video proudy v reálném čase mezi vzdálenými produkčními místy (jako sportovní stadiony nebo místa zpravodajských událostí) a centrálními vysílacími zařízeními. Služba pracuje na standardní infrastruktuře 5G NR, ale s konkrétními vylepšeními pro splnění přísných požadavků vysílacích médií, včetně ultranízké latence, vysoké spolehlivosti a konzistentní kvality služby.

Z architektonického hlediska BAS integruje požadavky vysílací služby do 5G core sítě a rádiové přístupové sítě. Mezi klíčové síťové funkce zapojené do procesu patří Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), které jsou konfigurovány pro vytváření a udržování vyhrazených QoS toků pro vysílací provoz. User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) zajišťuje přepojování mediálních proudů s odpovídající prioritizací a tvorbou provozu. Na rádiové straně jsou gNB konfigurovány tak, aby poskytovaly stabilní vysokopropustnostní připojení s minimálním kolísáním, často s využitím síťového řezání pro izolaci vysílacího provozu od ostatních mobilních služeb.

BAS funguje tak, že mezi vysílacím zařízením (kamery, audio mixážní pulty) vybaveným 5G modemem a mediální bránou vysílacího centra vytváří zabezpečené spojení typu point-to-point nebo point-to-multipoint. Služba využívá specifické QoS Class Identifiers (QCIs) a 5G QoS Indicators (5QIs) přizpůsobené pro přenos médií v reálném čase, což zajišťuje garantované přenosové rychlosti, maximální rozpočty zpoždění paketů a míry chybovosti paketů odpovídající profesionální vysílací kvalitě. Systém podporuje dynamickou alokaci šířky pásma a dokáže se přizpůsobit měnícím se síťovým podmínkám při zachování integrity mediálního proudu.

Kritickou součástí je Broadcast Service Manager ([BSM](/mobilnisite/slovnik/bsm/)), který může být implementován jako aplikační funkce nebo funkce pro vystavení sítě. BSM komunikuje s vysílacími operačními systémy pro žádosti o síťové prostředky, monitorování výkonu služby a správu smluv o úrovni služeb. Služba také zahrnuje přesnou synchronizaci času využitím funkcí 5G pro časování a synchronizaci, což je nezbytné pro sladění více kamerových přenosů a audio zdrojů v živých produkčních prostředích. BAS představuje konvergenci telekomunikačních a vysílacích technologií, umožňující flexibilní a nákladově efektivní možnosti vzdálené produkce.

## K čemu slouží

BAS byla vytvořena pro řešení rostoucí potřeby flexibilních, mobilních a nákladově efektivních řešení pro příspěvkové spoje vysílání. Tradiční vysílací operace jsou silně závislé na satelitních vozech, vyhrazených mikrovlnných spojích nebo optických okruzích pro přenos živých přenosů z odlehlých míst. Tyto metody jsou nákladné na nasazení, postrádají mobilitu a mají dlouhou dobu přípravy. Rozšíření sítí 5G představovalo příležitost využít všudypřítomnou mobilní konektivitu pro profesionální vysílací aplikace, ale standardní služby 5G pro spotřebitele postrádaly spolehlivost, záruky kvality a možnosti správy vyžadované pro vysílání.

Primární problém, který BAS řeší, je umožnit vysílacím organizacím využívat komerční sítě 5G jako spolehlivý přenosový prostředek pro živý obsah vysoké hodnoty. Řeší konkrétní technické výzvy, včetně udržování konzistentní kvality videa během mobility, zajištění ultranízké latence pro pracovní postupy živé produkce, poskytování přesné synchronizace pro vícekamerová nastavení a garance dostupnosti služby i v podmínkách přetížené sítě. Definováním standardizovaných rozhraní a procedur v rámci 3GPP zajišťuje BAS interoperabilitu mezi vysílacím zařízením od různých výrobců a sítěmi 5G od různých operátorů.

Historicky museli vysílatelé buď nasazovat vlastní privátní sítě, nebo se spoléhat na specializované poskytovatele služeb pro příspěvkové spoje. BAS jim umožňuje využívat veřejnou infrastrukturu 5G při zachování výkonu na úrovni vysílání prostřednictvím síťového řezání, vylepšených mechanismů QoS a specializované správy služeb. Tím se snižují kapitálové výdaje na vyhrazené vysílací přenosové zařízení a zvyšuje se provozní flexibilita, což umožňuje vysílatelům rychle nasadit dočasné pokrytí na událostech bez rozsáhlé přípravy infrastruktury. Technologie podporuje průmyslový trend směrem k vzdálené produkci a vysílacím pracovním postupům založeným na cloudu.

## Klíčové vlastnosti

- Garantovaná QoS s parametry 5QI specifickými pro vysílání pro latenci a ztrátu paketů
- Podpora point-to-point a point-to-multipoint distribuce médií
- Integrace se síťovým řezáním pro izolaci služby a garance prostředků
- Přesná synchronizace času pro sladění více zdrojů médií
- Dynamická adaptace šířky pásma při zachování kvality služby
- Rozhraní pro správu služby pro integraci s vysílacími operačními systémy

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR

---

📖 **Anglický originál a plná specifikace:** [BAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/bas/)
