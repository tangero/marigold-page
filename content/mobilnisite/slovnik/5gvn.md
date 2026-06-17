---
slug: "5gvn"
url: "/mobilnisite/slovnik/5gvn/"
type: "slovnik"
title: "5GVN – 5G Virtual Network"
date: 2026-01-01
abbr: "5GVN"
fullName: "5G Virtual Network"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/5gvn/"
summary: "5G virtuální síť (5GVN) je spravovaná komplexní komunikační služba pro podnikové zákazníky vybudovaná nad veřejnou síťovou infrastrukturou 5G. Poskytuje izolované, přizpůsobitelné připojení se zaručen"
---

5GVN je spravovaná komplexní komunikační služba pro podniky, která poskytuje izolované a přizpůsobitelné připojení přes veřejnou infrastrukturu 5G a umožňuje služby podobné privátní síti bez nutnosti vlastnit fyzickou síť.

## Popis

5G virtuální síť (5GVN) je standardizovaný koncept služby definovaný organizací 3GPP, který umožňuje mobilním síťovým operátorům (MNO) nabízet podnikovým zákazníkům spravované komplexní komunikační služby. V zásadě se jedná o logickou overlay síť vytvořenou pomocí základních schopností veřejného 5G systému (5GS), včetně síťového řezání (Network Slicing), rámců QoS a řízení politik. 5GVN není fyzická síť, ale abstrakce služby, která poskytuje vyhrazené, izolované a přizpůsobitelné komunikační prostředí pro konkrétní podnik nebo skupinu uživatelů s definovanými charakteristikami výkonu a rozhraními pro správu.

Z architektonického hlediska je 5GVN realizována koordinovanou konfigurací více síťových funkcí 5G. Jejím základem je vyhrazený síťový řez (Network Slice) nebo sada řezů, které zajišťují izolaci prostředků a oddělení provozu. Servisní model 5GVN pak na tento řez přidává parametry služby vyšší úrovně, možnosti správy a expoziční funkce. Mezi klíčové zapojené komponenty patří funkce pro výběr síťového řezu (NSSF), funkce řízení politik (PCF) pro vynucování politik specifických pro službu, jednotná správa dat (UDM) pro správu předplatného a funkce expozice sítě (NEF) pro bezpečné vystavení síťových schopností a správy služeb podniku nebo poskytovateli služeb třetí strany.

Provoz 5GVN začíná její zřízením, což zahrnuje definici profilu služby operátorem (MNO). Tento profil obsahuje parametry jako sada registrovaného uživatelského zařízení (UE), geografická oblast služby, požadovaný síťový řez (nebo řezy), specifické profily QoS (např. garantovaná přenosová rychlost, latence), pravidla řízení přístupu a povolená jména datových sítí (DNN). Když se registrované UE připojí k síti, 5G jádro identifikuje jeho asociaci s 5GVN a směruje jeho provoz příslušně nakonfigurovanou instancí řezu, přičemž aplikuje definované politiky pro správu relací, mobilitu a účtování.

Úlohou 5GVN v síti je překlenout propast mezi základními síťovými schopnostmi a využitelnými obchodními službami. Poskytuje standardizovaný rámec, který umožňuje operátorům produktizovat a zpeněžit pokročilé funkce 5G, jako je síťové řezání, a přeměnit je na fakturovatelné, zákazníkem částečně spravovatelné služby. Pro podnik nabízí zážitek z 'virtuální privátní sítě' se smlouvami SLA, samoobslužnými portály pro omezenou správu (přes vystavená API) a bezproblémovou integraci s jejich stávajícími IT systémy, a to vše bez kapitálových výdajů a provozní zátěže spojené s nasazením fyzicky oddělené RAN a jádrové sítě.

## K čemu slouží

Koncept 5G virtuální sítě byl zaveden, aby uspokojil rostoucí poptávku vertikálních odvětví (např. výroba, logistika, energetika) po vysoce výkonných, spolehlivých a bezpečných privátních mobilních sítích. Zatímco tradiční podniková řešení, jako jsou VPN přes internet typu best-effort, postrádají záruky výkonu, a vyhrazené privátní sítě jsou nákladné a složité na nasazení, 5GVN nabízí střední cestu. Využívá obrovského rozsahu a pokročilých funkcí veřejné infrastruktury 5G k poskytování schopností podobných privátní síti jako službu, čímž řeší problémy vysoké počáteční investice, licencování spektra a specializovaných provozních znalostí vyžadovaných pro plně privátní nasazení.

Historicky nabízely předchozí generace mobilních sítí omezené mechanismy pro přizpůsobení sítě podnikům, primárně prostřednictvím přístupových bodů (APN) se základní QoS, kterým chyběla izolace, podrobné řízení politik a standardizovaná rozhraní pro správu služeb. Motivací pro vytvoření 5GVN ve verzi Release 17 bylo poskytnout standardizovaný, operátorem spravovaný servisní model, který plně využívá nativní podporu 5G systému pro síťové řezání, edge computing a architekturu založenou na službách. Tato standardizace je klíčová pro zajištění interoperability mezi operátory a dodavateli zařízení, umožňuje globální poskytování služeb a podporuje živoucí ekosystém poskytovatelů služeb a podnikových řešení.

5GVN navíc umožňuje nové obchodní modely pro mobilní síťové operátory, kteří se tak mohou posunout za pouhou konektivitu a stát se hybateli digitální transformace průmyslu. Řeší omezení veřejného mobilního širokopásmového připojení typu 'jedna velikost pro všechny' tím, že poskytuje rámec pro vytváření šitých síťových služeb se specifickými atributy výkonu, zabezpečení a správy, čímž odemyká výnosový potenciál 5G na trzích business-to-business (B2B) a business-to-business-to-consumer (B2B2C).

## Klíčové vlastnosti

- Komplexní logická izolace prostřednictvím základních síťových řezů (Network Slices)
- Přizpůsobitelné výkonnostní profily se zaručenou QoS (např. latence, spolehlivost)
- Standardizovaná správa životního cyklu služby (vytvoření, změna, ukončení)
- Vystavení síťových schopností a správy služeb prostřednictvím API NEF
- Podpora integrace s podnikovými IT systémy a aplikacemi
- Flexibilní definice rozsahu služby (např. konkrétní UE, geografické oblasti, časová období)

## Definující specifikace

- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals

---

📖 **Anglický originál a plná specifikace:** [5GVN na 3GPP Explorer](https://3gpp-explorer.com/glossary/5gvn/)
