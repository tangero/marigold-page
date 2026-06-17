---
slug: "etftn"
url: "/mobilnisite/slovnik/etftn/"
type: "slovnik"
title: "ETFTN – Extended TFT Support Network"
date: 2025-01-01
abbr: "ETFTN"
fullName: "Extended TFT Support Network"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/etftn/"
summary: "Síťová schopnost, která umožňuje uživatelskému zařízení (UE) navázat více kontextů protokolu přenosu datových paketů (PDP) nebo relací přenosu datových jednotek (PDU) asociovaných s jedinou IP adresou"
---

ETFTN je síťová schopnost, která umožňuje uživatelskému zařízení (UE) navázat více kontextů PDP nebo relací PDU s jedinou IP adresou, přičemž každý má svou vlastní šablonu toku provozu (Traffic Flow Template) pro pokročilé řízení kvality služeb (QoS) a diferenciaci služeb.

## Popis

Extended TFT Support Network (ETFTN) je funkce jádra sítě [GPRS](/mobilnisite/slovnik/gprs/)/EPC definovaná v 3GPP TS 23.060. Rozšiřuje mechanismus tradiční šablony toku provozu (Traffic Flow Template – TFT). TFT je sada paketových filtrů (založených na IP adresách, číslech portů, typech protokolů) používaných ke klasifikaci downlinkového IP provozu a jeho mapování na konkrétní přenosový kanál (bearer) s definovanou kvalitou služeb (QoS). Obvykle pro danou IP adresu přiřazenou uživatelskému zařízení (UE) veškerý provoz odpovídající TFT primárního kontextu PDP proudí tímto kontextem. ETFTN umožňuje síti podporovat 'sekundární kontexty PDP' (v 3G/GPRS) nebo vyhrazené přenosové kanály (dedicated bearers) (v 4G/5G), které sdílejí stejnou IP adresu jako primární kontext, ale mají odlišné TFT a profily QoS.

Z architektonického hlediska funkce zahrnuje koordinaci mezi uživatelským zařízením (UE), uzlem SGSN (Serving GPRS Support Node) v 3G, nebo entitou [MME](/mobilnisite/slovnik/mme/)/funkcí [SMF](/mobilnisite/slovnik/smf/) (Mobility Management Entity/Session Management Function) v 4G/5G a uzlem GGSN/bránou PGW/funkcí [UPF](/mobilnisite/slovnik/upf/) (Gateway GPRS Support Node/PDN Gateway/User Plane Function). Když aplikace na uživatelském zařízení vyžaduje specifickou QoS (např. nízkou latenci pro VoIP), může uživatelské zařízení požádat o aktivaci sekundárního kontextu PDP nebo vyhrazeného přenosového kanálu. Tato žádost obsahuje novou TFT, která popisuje tok provozu pro danou aplikaci. Síť žádost autorizuje na základě zásad předplatitele a vytvoří nový logický přenosový kanál (s vlastním identifikátorem třídy QoS – [QCI](/mobilnisite/slovnik/qci/)/[5QI](/mobilnisite/slovnik/5qi/), garantovanou přenosovou rychlostí atd.) mezi uživatelským zařízením a bránou, přičemž všechny sdílejí stejnou IP adresu jako výchozí přenosový kanál.

Jak to funguje: Ve směru downlink brána (GGSN/PGW/UPF) kontroluje příchozí pakety pro IP adresu uživatelského zařízení. Poté aplikuje paketové filtry ze všech aktivních TFT asociovaných s touto IP adresou. Paket je směrován na přenosový kanál, jehož TFT mu odpovídá. Pokud odpovídá více TFT, uplatňují se pravidla priority a pořadí vyhodnocení. Ve směru uplink uživatelské zařízení provádí stejnou klasifikaci a směruje svůj vlastně generovaný provoz do příslušného přenosového kanálu na základě uplinkových paketových filtrů ve svých TFT. To umožňuje síti poskytovat podrobné řízení QoS, účtování a zásad na základě jednotlivých aplikačních toků, aniž by vyžadovala více IP adres pro uživatelské zařízení, čímž zjednodušuje správu sítě a šetří adresy IPv4.

## K čemu slouží

ETFTN byl vyvinut k řešení omezení základního modelu kontextu PDP, který vázal jednu IP adresu k jednomu profilu QoS. Když mobilní zařízení začala současně provozovat více aplikací (např. prohlížení webu, e-mail, hlasový hovor, streamování videa), potřebovala způsob, jak získat různé úrovně QoS pro různé typy provozu bez režie a spotřeby zdrojů spojených s navazováním zcela samostatných IP připojení (každé s vlastní IP adresou). Problémem bylo umožnit skutečnou diferenciaci služeb pro služby IMS, jako je VoLTE, kde hlasové pakety vyžadují přenosový kanál s garantovanou přenosovou rychlostí a nízkou latencí, zatímco datový provoz na pozadí využívá kanál s best-effort QoS.

Motivace vycházela z potřeby efektivně podporovat služby IMS a další služby v reálném čase přes paketově přepínané sítě. Před zavedením ETFTN mohlo dosažení různých úrovní QoS vyžadovat více kontextů PDP s více IP adresami, což komplikovalo směrování, účtování a překlad síťových adres ([NAT](/mobilnisite/slovnik/nat/)). ETFTN to řeší tím, že umožňuje multiplexovat více kanálů QoS (přenosových kanálů) přes jedno přiřazení IP adresy. To je efektivnější pro síť (potřeba méně IP adres, jednodušší stav směrování) i pro zařízení (sdílená konfigurace IP zásobníku).

Poskytuje základní mechanismus pro síťově řízenou QoS, který je klíčový pro zajištění konzistentní kvality služeb pro hlas a video přes IP. Umožňuje operátorům implementovat pravidla řízení zásad a účtování (PCC), která spouštějí vytváření specifických vyhrazených přenosových kanálů pro konkrétní služby, čímž zajišťují optimální využití zdrojů a uživatelský zážitek. Jeho vývoj napříč vydáními standardů byl spojen s vylepšováním architektury PCC a zaváděním nových parametrů QoS pro pokročilé služby.

## Klíčové vlastnosti

- Umožňuje více kontextům PDP/relacím PDU s odlišnými profily QoS sdílet jedinou IP adresu uživatelského zařízení (UE).
- Využívá šablony toku provozu (TFT) obsahující uplinkové a downlinkové paketové filtry pro klasifikaci provozu.
- Umožňuje dynamické vytváření sekundárních/vyhrazených přenosových kanálů spouštěné požadavkem aplikace nebo síťovou politikou.
- Poskytuje podrobné řízení QoS na základě jednotlivých aplikačních toků (např. samostatné přenosové kanály pro hlas, video, data).
- Klíčové pro umožnění služeb IMS, jako je VoLTE a ViLTE, s přenosovými kanály s garantovanou přenosovou rychlostí.
- Integruje se s architekturou řízení zásad a účtování (PCC) pro autorizaci a správu přenosových kanálů.

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [ETFTN na 3GPP Explorer](https://3gpp-explorer.com/glossary/etftn/)
