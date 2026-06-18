---
slug: "sgm-s"
url: "/mobilnisite/slovnik/sgm-s/"
type: "slovnik"
title: "SGM-S – SEAL Group Management Server"
date: 2025-01-01
abbr: "SGM-S"
fullName: "SEAL Group Management Server"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sgm-s/"
summary: "SEAL Group Management Server (SGM-S) je základní síťová funkce zavedená ve 3GPP Release 16 pro správu skupin SEAL (SErvice Access Layer). Zajišťuje správu členství ve skupině, konfiguraci a vynucování"
---

SGM-S je základní síťová funkce pro správu skupin SEAL, která zajišťuje správu jejich členství, konfigurace a politiky, aby umožnila efektivní skupinovou komunikaci a správu zdrojů.

## Popis

[SEAL](/mobilnisite/slovnik/seal/) Group Management Server (SGM-S) je klíčová komponenta v architektuře 3GPP pro správu skupin Service Access Layer (SEAL). SEAL je rámec navržený pro poskytování efektivních skupinových komunikačních služeb, zvláště relevantních pro IoT a [V2X](/mobilnisite/slovnik/v2x/) aplikace. SGM-S funguje jako centrální autorita pro tyto skupiny a sídlí v základní síti. Jeho primární funkcí je vytváření, modifikace, rušení a celková správa životního cyklu skupin SEAL. Spravuje databázi členství ve skupinách, která může obsahovat identifikátory UE (User Equipment), a je zodpovědný za distribuci konfiguračních informací skupiny příslušným síťovým entitám, jako je SEAL Group Management Client (SGM-C) v UE nebo jiné síťové funkce.

Z architektonického hlediska SGM-S komunikuje s dalšími funkcemi základní sítě prostřednictvím standardizovaných rozhraní definovaných ve specifikacích jako 24.544. Přijímá požadavky na operace správy skupin, tyto požadavky ověřuje a autorizuje a následně provádí potřebné akce. To zahrnuje poskytování skupinových politik, které určují, jak má být skupinová komunikace zpracována – například definici parametrů QoS, bezpečnostních kontextů nebo pravidel směrování pro skupinový provoz. SGM-S zajišťuje konzistenci a synchronizaci stavu skupiny v celé síti, což je zásadní pro služby, kde musí více UE jednat koordinovaně na základě své skupinové příslušnosti.

Z provozního pohledu SGM-S funguje zpracováním příkazů správy. Když má být zřízena nová skupina SEAL, například pro flotilu připojených vozidel nebo sadu průmyslových senzorů, autorizovaná entita (jako aplikační server nebo síťový administrátor) odešle požadavek na SGM-S. Server požadavek ověří, vytvoří záznam skupiny, přiřadí jedinečné Group ID a definuje počáteční členství a politiky. Tyto informace následně šíří. V průběžné správě SGM-S zajišťuje přidávání a odebírání členů, aktualizace politik a rozpuštění skupiny. Jeho role je čistě řídicí a správní; přímo nezpracovává datový provoz členů skupiny, ale poskytuje potřebné informace řídicí roviny, aby ostatní síťové funkce (jako User Plane Function nebo přístupové uzly) mohly správně zpracovat komunikační toky skupiny.

## K čemu slouží

SGM-S byl vytvořen, aby řešil potřebu škálovatelné a efektivní správy skupinových služeb v mobilních sítích. Před jeho zavedením skupinová komunikace (např. pro IoT nebo veřejnou bezpečnost) často spoléhala na ad-hoc metody nebo správu na aplikační vrstvě, což postrádalo integraci s řídicí rovinou sítě. To vedlo k neefektivitám, špatnému využití zdrojů a obtížím při jednotném uplatňování síťových politik, jako je QoS nebo bezpečnost, na skupinu. Rámec [SEAL](/mobilnisite/slovnik/seal/) včetně SGM-S byl motivován rostoucí poptávkou po komunikaci [V2X](/mobilnisite/slovnik/v2x/) (Vehicle-to-Everything) a nasazeními masivního IoT, kde je třeba s tisíci zařízeními zacházet jako s logickou skupinou pro účely komunikace a správy.

Historicky správa skupin UE vyžadovala individuální signalizaci každému členovi nebo spoléhala na techniky vysílání/vícebodového vysílání bez jemně odstupňované kontroly. SGM-S poskytuje standardizované, síťově integrované řešení. Řeší problém centralizované, autoritativní správy skupin, což síti umožňuje optimalizovat zdroje tím, že se se skupinou pro určité řídicí procedury zachází jako s jedinou entitou. Tím se snižuje signalizační režie a umožňuje uplatňování skupinově specifických politik, které jsou vynucovány samotnou sítí, což vede k spolehlivějším a výkonnějším skupinovým službám. Jeho vytvoření v Release 16 je v souladu s širšími snahami 3GPP o zlepšení podpory pokročilých služeb, jako jsou automobilové a průmyslové IoT, kde jsou skupinové dynamiky zásadní.

## Klíčové vlastnosti

- Centralizovaná správa životního cyklu (vytváření, modifikace, rušení) skupin SEAL
- Údržba databází členství ve skupinách a distribuce informací o členství
- Poskytování a vynucování skupinově specifických politik (QoS, bezpečnost, směrování)
- Interakce s klientskou stranou SGM-C v UE pro komplexní správu skupin
- Standardizovaná rozhraní (definovaná v 24.544) pro integraci s dalšími funkcemi základní sítě
- Podpora ověřování a autorizace operací správy skupin

## Související pojmy

- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 24.544** (Rel-19) — SEAL Group Management Protocol

---

📖 **Anglický originál a plná specifikace:** [SGM-S na 3GPP Explorer](https://3gpp-explorer.com/glossary/sgm-s/)
